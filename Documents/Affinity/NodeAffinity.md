# Node Affinity
İki Farklı Şekilde Node Affinity'ı Kullanabiliriz.
* requiredDuringSchedulingIgnoredDuringExecution
 Çok katı kural Nodeselector Pod Schedule edilmeden kural sağlanmalı
* preferredDuringSchedulingIgnoredDuringExecution
  kuralın gerçekleşmesi için girişimde bulunur ama kuralın gerçekleştiğini garanti etmez
  Weight değeri kullanılabilir.
  