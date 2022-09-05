# BLOG DE EXPERIENCIAS

Descargar y ejecutar rama-belu-prueba-merge. Por el momento es la única que están
tanto actualizada con todos los requerimientos como funcionando.

## Descripción del Proyecto: 
Es un blog en donde se registran experiencias recreativas en Argentina.
La experiencia esta relacionada a una provincia y actividad cargadas previamente.
La experiencia es generada por un usuario, que deja asentado qué actividad hizo,
en qué provincia y deja un pequeño comentario en que nos cuenta cómo la pasó.

## Estado del proyecto: Inicial

## Demostración de funciones y aplicaciones:
El sitio está dividido, de momento, en cinco partes que equivalen a las cinco páginas.

**INICIO**: que nos lleva a la página principal. En esta primera instancia, aparece en cada
una de las páginas, pero la idea es que sólo aparezca en todas aquellas páginas que
NO SEAN index.html

**EXPERIENCIAS**: que nos lleva a la página central, si se quiere, del sitio. En ella encontramos
los siguientes campos:
- *Provincia*: donde el user podrá elegir de una lista desplegable el repertorio de provincias
de la Argentina para determinar dónde realizó la actividad.
- *Actividad*: como con el campo anterior, el user elije una actividad de la lista desplegable. En
esta instancia inicial, hemos decidido ingresar los datos que componen la lista de manera manual, 
pero la idea en última instancia es que podamos traer todas las actividades cargadas desde la
base de datos, sin necesidad de cargarlas a mano.
- *Usuario*: nuevamente una lista desplegable. Las opciones disponibles han sido agregadas manualmente pero la idea es que este campo ya no sea necesario porque ya habremos creado el
LOGIN para que cada user se pueda crear su perfil y pueda comenzar a compartir.
- *Experiencia*: en este cuadro de texto el user debe contarnos su experiencia en 140 caracteres
o menos.
- *Fecha experiencia*: campo para que el user pueda asignar la fecha en que llevó adelante la
actividad.
- *Enviar*: apretando este btón se guarda en la base de datos la experiencia y se refresca el
formulario.

**¿EN QUÉ PROVINCIA?**: allí encontraremos el formulario para que cada usuario pueda ir agregando las provincias que ha visitado. [Es muy probable que esta página sea modificada o eliminada. Por
el momento dado, quedará así.]
- *Código*: valor key para cada registro. Se eliminará en versiones futuras, pero por una cuestión
de conocimiento básico sobre báse de datos, quedará por el momento.
- *Nombre*: nombre de la provincia.
- *Zona*: sector de la provincia en que se realizó la actividad.
- *Descripción*: una breve descripción del clima y fauna de dicha provincia.
- *Enviar*: ídem. anterior página.

**¿QUÉ ACTIVIDAD?**: otro formulario. Aquí los users registran el tipo de actividad realizada y
en qué consiste. Nótese la presencia de un campo idéntico a la página anterior, *código*. Existe
por la misma razón que en el caso anterior y será, probablemente, eliminado también por la misma
causa.

**¿QUÉ USUARIO?**: este es un estadío precario de nuestro SIGN-IN, donde se registrarán los users.
De momento, esta sección servirá como formulario de registro. Hay grandes probabilidades de que
en versiones posteriores aparezca bajo la label de "REGISTRATE".