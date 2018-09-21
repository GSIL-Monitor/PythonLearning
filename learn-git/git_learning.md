### gitlib
git --help
git add NjxJsonPresingMR.jar
git commit -m "add NjxJsonPresingMR.jar "
git push
git pull

```
# git没法push问题 ! [rejected] master -> master (non-fast-forward)
git merge origin/master  --allow-unrelated-histories
git push --all
git add -A
git commit -m "change massage"
git push origin master
git status
```

### 配置github和gitlib双通

ssh-keygen -t rsa -C "wangchenchen@babyfs.cn" -b 4096
gitlab_id_rsa
ssh -T git@gitlib.babyfs.cn

ssh-keygen -t rsa -C "249398363@qq.com"
github_id_rsa
ssh -T git@github.com

config内容
```
#gitlab
Host gitlab.babyfs.cn
hostname gitlab.babyfs.cn
IdentityFile ~/.ssh/gitlab_id_rsa

#github
Host github.com
user 249398363@qq.com
HostName ssh.github.com
preferredAuthentications publickey
IdentityFile ~/.ssh/github_id_rsa
```

### 本地项目同步到github
```
$ cd learn-python
$ git init
$ git remote add origin git@github.com:shasky2014/PythonLearning.git
$ git pull origin master
$ git add -A
$ git commit -m 'cccccc'
$ git push --set-upstream origin master
```

