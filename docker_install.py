#
# 1. 在Ubuntu中安装Docker
# 更新ubuntu的apt源索引
#
# sudo apt-get update
# 安装包允许apt通过HTTPS使用仓库
#
# sudo apt-get install \
#     apt-transport-https \
#     ca-certificates \
#     curl \
#     software-properties-common
# 添加Docker官方GPG key
#
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# 设置Docker稳定版仓库
#
# sudo add-apt-repository \
#    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
#    $(lsb_release -cs) \
#    stable"
# 添加仓库后，更新apt源索引
#
# sudo apt-get update
# 安装最新版Docker CE（社区版）
#
# sudo apt-get install docker-ce
# 检查Docker CE是否安装正确
#
# sudo docker run hello-world
# 出现如下信息，表示安装成功
#
# hello world
#
# 为了避免每次命令都输入sudo，可以设置用户权限，注意执行后须注销重新登录
#
# sudo usermod -a -G docker $USER
# 2. 启动与停止
# 安装完成Docker后，默认已经启动了docker服务，如需手动控制docker服务的启停，可执行如下命令
#
# # 启动docker
# sudo service docker start
#
# # 停止docker
# sudo service docker stop
#
# # 重启docker
# sudo service docker restart
# 3. Docker镜像操作
# 什么是Docker镜像
# Docker 镜像是由文件系统叠加而成(是一种文件的存储形式)。最底端是一个文件引 导系统，即 bootfs，这很像典型的 Linux/Unix 的引导文件系统。Docker 用户几乎永远不会和 引导系统有什么交互。实际上，当一个容器启动后，它将会被移动到内存中，而引导文件系 统则会被卸载，以留出更多的内存供磁盘镜像使用。Docker 容器启动是需要一些文件的， 而这些文件就可以称为 Docker 镜像。
#
# docker 镜像
#
# Docker 把应用程序及其依赖，打包在 image 文件里面。只有通过这个文件，才能生成 Docker 容器。image 文件可以看作是容器的模板。Docker 根据 image 文件生成容器的实例。同一个 image 文件，可以生成多个同时运行的容器实例。
#
# image 是二进制文件。实际开发中，一个 image 文件往往通过继承另一个 image 文件，加上一些个性化设置而生成。举例来说，你可以在 Ubuntu 的 image 基础上，往里面加入 Apache 服务器，形成你的 image。
#
# image 文件是通用的，一台机器的 image 文件拷贝到另一台机器，照样可以使用。一般来说，为了节省时间，我们应该尽量使用别人制作好的 image 文件，而不是自己制作。即使要定制，也应该基于别人的 image 文件进行加工，而不是从零开始制作。
#
# 为了方便共享，image 文件制作完成后，可以上传到网上的仓库。Docker 的官方仓库 Docker Hub 是最重要、最常用的 image 仓库。此外，出售自己制作的 image 文件也是可以的。
#
# 列出镜像
# docker image ls
# 列出镜像
#
# REPOSITORY：镜像所在的仓库名称
# TAG：镜像标签
# IMAGEID：镜像ID
# CREATED：镜像的创建日期(不是获取该镜像的日期)
# SIZE：镜像大小
# 为了区分同一个仓库下的不同镜像，Docker 提供了一种称为标签(Tag)的功能。每个 镜像在列出来时都带有一个标签，例如latest、 12.10、12.04 等等。每个标签对组成特定镜像的一 些镜像层进行标记(比如，标签 12.04 就是对所有 Ubuntu12.04 镜像层的标记)。这种机制 使得同一个仓库中可以存储多个镜像。--- 版本号
#
# 我们在运行同一个仓库中的不同镜像时，可以通过在仓库名后面加上一个冒号和标签名 来指定该仓库中的某一具体的镜像，例如 docker run --name custom_container_name –i –t docker.io/ubunto:12.04 /bin/bash，表明从镜像 Ubuntu:12.04 启动一个容器，而这个镜像的操 作系统就是 Ubuntu:12.04。在构建容器时指定仓库的标签也是一个好习惯。
#
# 拉取镜像
# Docker维护了镜像仓库，分为共有和私有两种，共有的官方仓库Docker Hub(https://hub.docker.com/)是最重要最常用的镜像仓库。私有仓库（Private Registry）是开发者或者企业自建的镜像存储库，通常用来保存企业 内部的 Docker 镜像，用于内部开发流程和产品的发布、版本控制。
#
# 要想获取某个镜像，我们可以使用pull命令，从仓库中拉取镜像到本地，如
#
# docker image pull library/hello-world
# 上面代码中，docker image pull是抓取 image 文件的命令。library/hello-world是 image 文件在仓库里面的位置，其中library是 image 文件所在的组，hello-world是 image 文件的名字。
#
# 由于 Docker 官方提供的 image 文件，都放在library组里面，所以它的是默认组，可以省略。因此，上面的命令可以写成下面这样。
#
# docker image pull hello-world
# 删除镜像
# docker image rm 镜像名或镜像id
# 如
#
# docker image rm hello-world
# 4. Docker 容器操作
# 创建容器
# docker run [option] 镜像名 [向启动容器中传入的命令]
# 常用可选参数说明：
#
# -i 表示以“交互模式”运行容器
# -t 表示容器启动后会进入其命令行。加入这两个参数后，容器创建就能登录进去。即 分配一个伪终端。
# --name 为创建的容器命名
# -v 表示目录映射关系(前者是宿主机目录，后者是映射到宿主机上的目录，即 宿主机目录:容器中目录)，可以使 用多个-v 做多个目录或文件映射。注意:最好做目录映射，在宿主机上做修改，然后 共享到容器上。
# -d 在run后面加上-d参数,则会创建一个守护式容器在后台运行(这样创建容器后不 会自动登录容器，如果只加-i -t 两个参数，创建后就会自动进去容器)。
# -p 表示端口映射，前者是宿主机端口，后者是容器内的映射端口。可以使用多个-p 做多个端口映射
# -e 为容器设置环境变量
# --network=host 表示将主机的网络环境映射到容器中，容器的网络与主机相同
# 交互式容器
# 例如，创建一个交互式容器，并命名为myubuntu
#
# docker run -it --name=myubuntu ubuntu /bin/bash
# 在容器中可以随意执行linux命令，就是一个ubuntu的环境，当执行exit命令退出时，该容器也随之停止。
#
# 守护式容器
# 创建一个守护式容器:如果对于一个需要长期运行的容器来说，我们可以创建一个守护式容器。在容器内部exit退出时，容器也不会停止。
#
# docker run -dit --name=myubuntu2 ubuntu
# 进入已运行的容器
# docker exec -it 容器名或容器id 进入后执行的第一个命令
# 如
#
# docker exec -it myubuntu2 /bin/bash
# 查看容器
# # 列出本机正在运行的容器
# docker container ls
#
# # 列出本机所有容器，包括已经终止运行的
# docker container ls --all
# 停止与启动容器
# # 停止一个已经在运行的容器
# docker container stop 容器名或容器id
#
# # 启动一个已经停止的容器
# docker container start 容器名或容器id
#
# # kill掉一个已经在运行的容器
# docker container kill 容器名或容器id
# 删除容器
# docker container rm 容器名或容器id
# 5. 将容器保存为镜像
# 我们可以通过如下命令将容器保存为镜像
#
# docker commit 容器名 镜像名
# 6. 镜像备份与迁移
# 我们可以通过save命令将镜像打包成文件，拷贝给别人使用
#
# docker save -o 保存的文件名 镜像名
# 如
#
# docker save -o ./ubuntu.tar ubuntu
# 在拿到镜像文件后，可以通过load方法，将镜像加载到本地
#
# docker load -i ./ubuntu.tar
