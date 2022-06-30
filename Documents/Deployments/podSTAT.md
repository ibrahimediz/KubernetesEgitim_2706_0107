## Pod Status
* Pending => POD kabul edildi ama koşmuyor
    - hala indiriliyor olabilir
    - üretimi zamanlanmış olabilir. 
* Succeded => POD başarılı bir şekilde sonlandırıldı. 
* Failed => POD en az bir container ile ilgili problem var
* Unknown => POD bilinmeyen bir durumda. Node çalışmaz Network
## Pod Conditions
  * Pod Scheduled => Zamanlama işlemi tamamlandı.
  * Pod Ready => POD başarılı bir şekilde hazır.
  * Initialized => POD içindeki containerlar başarılı bir şekilde başlatıldı
  * Unschedulable => Sistem Kaynakları yetersiz.
  * ContainerReady => POD içindeki containerlar başarılı bir şekilde başlatıldı

## Container State:
    1. Running
    2. Terminating