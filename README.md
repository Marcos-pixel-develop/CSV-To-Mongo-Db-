# CSV-To-Mongo-Db-
This project creates a function that given a CSV file, it creates a Database Mongo Db with the same data

#Paso 1 
Se importan las librerias y la clase ConvertMongo, se crea el objeto tipo ConvertMongo y se le pasan los parametros de la base de datos, la colleccion y la cadena de conección que tiene el localhost

#Paso 2

Se puede usar ConvertCsv como ConvertCvdstr, la primera recibe un dataframe, mientras que la segunda el nombre del dataframe en los archivos. Ambos hacen la actualización de la base de datos en mongoDb según los datos
que se administraron por el dataframe
