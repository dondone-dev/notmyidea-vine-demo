title: Lets Encrypt and HTTP2
date: 2016-07-29 21:28:00
id: 1469776945
Category: Feature
tags: HTTPS, Nginx


![http2](https://images.yasking.org/technology/1469776945/01.png)


好长时间没更新博客，博客放在Github一直很安逸，但是前一段时间看到[@屈屈](https://imququ.com) 的博客就又想折腾了

之前Vultr主机充值多少送多少活动的时候充值了$25(+$25)，买了5刀每月的主机，正好可以用来折腾折腾

<!-- more -->

本篇主要记录操作记录，以及一些零零散散的东西，如果你也打算搭建个HEXO + HTTPS + HTTP2的博客，这篇文章会对你有些帮助，我记录的这个类似step by step，去屈屈的博客你能收获更多

我的VPS安装的Centos 7操作系统

### 安装Nginx

```shell
yum groupinstall "Development Tools"

yum install pcre-devel zlib-devel

# 下载最新的nginx
wget http://nginx.org/download/nginx-1.11.3.tar.gz
tar zxvf nginx-1.11.3.tar.gz

# 自己下载openssl是因为系统自带的openssl不支持ALPN，会导致浏览器访问降级为HTTP1.1
wget -O openssl.zip -c https://github.com/openssl/openssl/archive/OpenSSL_1_0_2h.zip unzip openssl.zip 
mv openssl-OpenSSL_1_0_2h/ openssl

wget -O nginx-ct.zip -c https://github.com/grahamedgecombe/nginx-ct/archive/v1.2.0.zip 
unzip nginx-ct.zip

# 编译三部曲
./configure --add-module=../nginx-ct-1.2.0 --with-openssl=../openssl --with-http_v2_module --with-http_ssl_module --with-ipv6 --with-http_gzip_static_module
make
make install
```

### 配置并启动nginx

```shell
/usr/local/nginx/sbin/nginx
```

打开浏览器，访问http://you.ip.addr 就可以看到nginx的hello world的

*PS: 访问不了可能是你的防火墙拦截了，试试在命令行输入iptables -F 临时关闭防火墙*

访问你的域名商，将你的域名指向到你的服务器

接下来对nginx进行简单的设置

修改nginx配置 `vim /usr/local/nginx/conf/nginx.conf`

```conf
server {
    listen       80;
    server_name  example.com;

    location / {
        root   /home/website/example.com;
        index  index.html index.htm;
    }

    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   html;
    }

}
```

重新载入配置 `/usr/local/nginx/sbin/nginx -s reload`


在root后配置的目录新建一个文件 `echo "hello world" > /home/website/example.com/index.html`  (注意替换)

通过你的博客域名(我的是example.com)，访问页面输出`hello world`则之前的配置完成


### 生成Lets Encrypt的证书

自动化脚本很多，我使用的是这个 [xdtianyu](https://github.com/xdtianyu/scripts/blob/master/lets-encrypt/README-CN.md)

```
wget https://raw.githubusercontent.com/xdtianyu/scripts/master/lets-encrypt/letsencrypt.conf
wget https://raw.githubusercontent.com/xdtianyu/scripts/master/lets-encrypt/letsencrypt.sh
chmod +x letsencrypt.sh
```

中文文档很详细，Lets encrypt会校验你的域名所属

需要注意的就是脚本中填写的地址要与nginx配置的root后的地址一致，因为校验的时候会在网站目录写一个文件，然后通过web访问确认

生成的文件

```text
.
├── ishell.chained.crt
├── ishell.crt
├── ishell.csr
├── ishell.me.key
├── letsencrypt-account.key
├── letsencrypt.conf
├── letsencrypt.sh
└── lets-encrypt-x3-cross-signed.pem
```

上边的文档说的很详细了，就不多说了，接下来配置nginx，加载证书，开启HTTPS

我的nginx的ssl配置如下：

```
server {
    listen       443 ssl;
    server_name  example.com;

    ssl_certificate      /home/ssl/ishell.chained.crt;
    ssl_certificate_key  /home/ssl/ishell.me.key;

    ssl_session_cache    shared:SSL:50m;
    ssl_session_timeout  1d;

    ssl_ciphers                EECDH+CHACHA20:EECDH+CHACHA20-draft:EECDH+AES128:RSA+AES128:EECDH+AES256:RSA+AES256:EECDH+3DES:RSA+3DES:!MD5;
    ssl_prefer_server_ciphers  on;

    location / {
        root   /home/website/ishell.me;
        index  index.html index.htm;
    }
}
```

`ssl_ciphers` 是我在屈屈的配置中摘的，因为默认配置下开启https没有问题，但是开启http2会失败

[《从启用 HTTP/2 导致网站无法访问说起》](https://imququ.com/post/why-tls-handshake-failed-with-http2-enabled.html) ， 这里详细的分析了原因

### 开启HTTP2

刚刚的配置，只需在`443 ssl`后面添加http2即可`443 ssl http2` 

重新载入nginx配置。在[https://tools.keycdn.com/http2-test](https://tools.keycdn.com/http2-test) 测试是否成功开启了HTTP2



### Hexo

使用nvm安装node

```shell
wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.31.3/install.sh | bash
exit   # 退出终端，重新登录以使环境变量生效
nvm install v5.0
node -v 
```

安装hexo

```shell
npm install hexo -g
hexo init blog
cd blog 
npm instal 
```

使用next主题

文档很齐全

- [http://theme-next.iissnan.com/](http://theme-next.iissnan.com/)
- [http://notes.iissnan.com/](http://notes.iissnan.com/)


### 生成静态文件

```
hexo g
```

修改blog目录下的_config.yml, 修改public_dir的路径为刚刚nginx配置的网站路径即可


一个基于Hexo的静态博客就开启HTTPS和HTTP2了

这里有个http2的演示~~ [https://http2.akamai.com/demo](https://http2.akamai.com/demo) 

对了，静态博客使用CDN也是很方便的，本站已经使用了keycdn，使用keycdn的时候还遇到一些问题。下一篇文章整理下全站使用key-cdn的方法，就先这样~












