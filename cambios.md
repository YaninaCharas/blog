:# Cambios propuestos─02/septiembre

## Modificaciones

- En **experiencias.html** borré todo porque repite contenido que tenemos en la página **index.html**, que será la página que utilizaremos de base y desde la que heredaremos a las demás páginas el estilo y la estructura.

A su vez, también me parece necesario pensar qué va a aparecer en este template. Lo que pensaba yo era que en este apareciera un listado de todas las entradas del blog, lo que quiere decir que tendremos ─esa parte me corresponde a mí─ que crear una vista que pueda mandarle de ***contexto*** una lista de todas las experiencias guardadas en la base de datos. (Si no se entiende, escribime y te mando un audio).

- En **views.py** borré la vista **provincias()** porque con ella lo único que hacíamos era insertar datos directamente a la base de datos, pero ahora que tenemos creada la vista **formulario_provincias()** podemos obtener esa misma información directamente desde el formulario.
- En **views.py**, también, coloqué todas las líneas de importación hacia el comienzo del documento más que nadas por razones de legibilidad y de convención a la hora de programar en Python.
- En **urls.py** agregué las urls necesarias para enlazar con las vistas de formularios. Eliminé a su vez el path de ‘experiencias’ porque enlazaba con la vista provincias() que, como ya te mencioné, eliminé.
- En **index.html** cambié las opciones en la barra de navegación para que nos llevara, al menos por esta instancia, a los formularios y a una pagina donde se muestre una lista de los usuarios (que por el momento seríamos vos y yo) a la que llegaríamos haciendo click sobre “Nosotras…”. Utilicé asignación de urls dinámicas, con el django template language que nos mostraron en las clase.

## Creaciones

- Dentro de Appblog, creé un archivo: **forms.py**. Allí residirán todos los formularios que necesitemos.
- Creé en **templates** un archivo-padre llamado ***formularios.html*** del que heredaremos la estructura de formulario a los templates correspondientes a cada modelo (**formulario_provincias**.html, **formulario_actividades**.html y **formulario_usuarios**.html, ya que se repetía la misma estructura en los tres.

##Modificaciones propuestas 3/9:

- Arregle en el index.html el Static para que toe el css del directorio correspondiente
- Comente en el formulario_base el navbar ya que generaba inconsistencias entre ese los html y el index.
- En la Class Provincias y actividades tienen que tener el codigo y tiene que ser unico

##Modificaciones/ 
- Modifique la vista de actividades (saque la provincia y agregue el codigo)
- Modifique las urls, tenian repetido la declaracion de formularios 2 veces
- Se cambio el title de index.html, se lo puso dinamico y paso al resto de los htmls
- Se agrego el Inicio en index.html "navbar-brand"
- Se para metrizo el navigation.html
- Se agregaron en admin.py los modelos para trabajarlos en el panel administrativo
- Se creo un superuser yanina 
