# Sentiment Analysist

Makine öğrenmesi ve Python programlama dili ile basit seviyede bir duygu analizi örneğidir.
Veri setimizi servisimiz üzerinden linkini gönderdiğimiz hepsiburada ürününün yorumlarını çekerek olumlu veya olumsuz şeklinde json dosyası içine ekler. Servisimiz üzerinden çekilen verileri python ile yazmış olduğumuz projenin içinde çağırarak onu csv dosyasına çevirerek algoritmamızı eğitiyoruz. Flask ile servis haline getirmiş olduğumuz makine öğrenmesi projemizi Asp.net MVC projesine bağlayarak yeni yorumların olumlumu olumsuzmu olduğunu değerlendirdik.

##### 'Positivity' Kolonu;
* 0 ise olumsuz yorum
* 1 ise olumlu yorum.

olarak kabul edilir.

---

It is an example of simple level emotion analysis with machine learning and Python programming language.
We will send the link of our data set via our service to the comments of Hepsiburada product and add it in  to the json file as positive or negative.We train our algorithm by calling the data taken from our service in the project we wrote with python and converting it to csv file. By linking our machine learning project, which we have made into service with Flask, to the Asp.net MVC project, we evaluated whether the new comments are negative.

##### 'Positivity' Column;
* 0 is negative comment
* 1 is a positive comment.

It is considered.

### Yararlanılan Kaynaklar / Utilized Resources
 * [Scikit-Learn for Text Analysis of Amazon Fine Food Reviews](https://datascienceplus.com/scikit-learn-for-text-analysis-of-amazon-fine-food-reviews/)
 * [trstop](https://github.com/ahmetax/trstop)
