# Docker for cgi with python(2.7, 3.6)

This is a simple python web server settings.  
With this docker image, you can create simple web application with cgi.  

## How to use
```bash
# build image
docker build -t pycgi_2 .
# run image
docker run \
-p 2345:80 \
-d \
-v your_git_path/docker-cgi-python/cgi-bin:/production/www/cgi-bin \
-v your_git_path/docker-cgi-python/www:/var/www/html \
--name mypycgi \
pycgi_2

# exec container
docker exec -it mypycgi /bin/bash
```

You can Access from the below URL.
* [http://localhost:2345](http://localhost:2345)
* [http://localhost:2345/test4.py](http://localhost:2345/cgi-bin2/test4.py)

## Allow Python version

* 2.7
* 3.6

### References

* [Usage of docker with apache2](https://www.dockerbook.com/code/6/jekyll/apache/Dockerfile)
* [【Linux】Rubyで書いたCGIをApacheで動かしてみる](http://note.kurodigi.com/apache-cgi/)

### Licence

* MIT
