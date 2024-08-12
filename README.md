一、解决Git连接失败
1.VPN环境下
打开“设置 -> 网络和Internet -> 代理”，记录下当前的端口号。
git config --global http.proxy 127.0.0.1:<你的端口号>
git config --global https.proxy 127.0.0.1:<你的端口号>
验证：git config --global -l
2.未使用VPN
git config --global --unset http.proxy
git config --global --unset https.proxy
