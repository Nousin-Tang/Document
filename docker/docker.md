##Docker常用命令

* 启动服务：`docker start 容器ID/容器名称`
* 停止服务：`docker stop 容器ID/容器名称`

* 删除容器：`docker rm 容器ID/容器名称`
* 删除镜像：`docker rmi 容器ID/REPOSITORY名称`

* 重命名镜像：`docker tag IMAGEID(镜像id)  名称【:TAG（标签）】`

* 保存镜像：`docker save 镜像名称  -o  保存文件的绝对位置（路径+文件名【扩展名为tar】）`
* 解压镜像：`docker load -i 文件名称.tar`
