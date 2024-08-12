一、解决Git连接失败
1.VPN环境下
打开“设置 -> 网络和Internet -> 代理”，记录下当前的端口号。
git config --global http.proxy 127.0.0.1:<你的端口号>
git config --global https.proxy 127.0.0.1:<你的端口号>
验证：git config --global -l
2.未使用VPN
git config --global --unset http.proxy
git config --global --unset https.proxy

二、Git相关指令
重命名分支      git branch -m oldBranchName newBranchName
新建并移动到分支git checkout -b branchname
建立本地分支和远程分支的关联（创建远程分支）git push --set-upstream origin branchname
拉取、提交、推送  1.git add .   2.git  commit -m "备注信息"   3.git pull   4.git push
查看本地分支    git branch
查看远程分支    git branch-a
