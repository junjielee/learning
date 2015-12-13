# Centos6 开发环境配置

## Nginx

1. 在/etc/yum.repos.d/目录添加nginx.repo文件，内容如下：
>
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/$releasever/$basearch/
gpgcheck=0
enabled=1

2. 使用yum install nginx 安装
3. 启动：/etc/init.d/nginx start

参考：[这里](https://gist.github.com/junjielee/808df867e1c2ddcf2747)

## sudo
1. yum install sudo
2. 编辑在/etc/sudoers,在root ALL=(ALL) ALL后面添加：
> username ALL=(ALL) ALL

参考：[这里](http://www.oschina.net/question/54100_23323)

## python2.7
```
sudo yum install openssl-devel gcc
wget https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tgz
tar xf Python-2.7.10.tgz
cd Python-2.7.10
./configure --prefix=/usr/local
make && sudo make install altinstall
```

## pip
参考[这里](http://pip-cn.readthedocs.org/en/latest/installing.html)，下载get-pip.py文件，然后使用python get-pip.py安装

## MySQL-python
1. yum install MySQL-python



## 帮助
1. rpm -qa | grep name ：查看是否安装了name