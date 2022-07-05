# bir noda taint eklemek için
```bash
kubectl taint nodes <node> <key>=<value>:<effect>
kubectl taint nodes minikube-m02 type=specialnode:NoSchedule
kubectl taint nodes minikube-m03 testanahtar=testdeger:NoExecute
```
