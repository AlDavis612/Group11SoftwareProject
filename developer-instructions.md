RJI project install and deploy.

AWS server config

  1.Install python3 on AWS server
  
    Download python3 source code package，then unzip it：
    tar -xvzf Python-3.5.1.tgz
    install 
    
  
  2.Install docker on AWS server

  3.Install JDK
  
    3.1 download jdk1.8，unzip jdk to path：/usr/java/jdk
      tar -xvf jdk-8u131-linux-x64.tar.gz -C /usr/java/jdk
    3.2 config environment path for jdk:
      vi /etc/profile
      add environment path to this file and save:
      #set java enviroment
      export JAVA_HOME=/usr/java/jdk/jdk1.8.0_131
      export JRE_HOME=/usr/java/jdk/jdk1.8.0_131/jre
      export CLASSPATH=.:$JAVA_HOME/lib$:JRE_HOME/lib:$CLASSPATH
      export PATH=$JAVA_HOME/bin:$JRE_HOME/bin/$JAVA_HOME:$PATH
      source /etc/profile
    3.3check jdk config ok:
      java -version
  4.Install Tomcat Apache
  
    4.1 download Tomcat8 and unzip to :
      tar -xvf apache-tomcat-8.5.14.tar.gz -C /usr/java/tomcat/
    4.2 edit tomcat8 bin/setclasspath.sh file, add two lines for jdk config at the bottom of this file
       export JAVA_HOME=/usr/java/jdk/jdk1.8.0_131
       export JRE_HOME=/usr/java/jdk/jdk1.8.0_131/jre

