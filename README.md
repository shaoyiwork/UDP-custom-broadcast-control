# UDP-custom-broadcast-control
this is a sample for your to remote control yanshee use udp broadcast

远程控制自编python文件（舞蹈动作等）执行步骤说明：

1、把listener文件夹拷贝到所有机器人身上

2、将udp_broadcast.py文件放到任意一台希望做发布控制命令的机器人上

3、将listener里面的your_python.py文件换成你编辑好的动作舞蹈动作文件（xxx.py）

4、将listener下面的udp_listener.py里面的那句os.system('sudo python your_python.py')里的your_python.py换成你自己的python文件名。

5、保存之后，所有要集控的机器人都运行 python udp_listener.py

6、用发控制命令的机器人打开终端命令行
   执行python udp_broadcast.py 文件 
   然后输入 start 
   随后其它机器人就可以一起做动作了
