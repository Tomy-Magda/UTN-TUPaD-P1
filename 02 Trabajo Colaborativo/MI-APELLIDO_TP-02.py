#TP2 Git y GitHub, Magdaleno Thomás. 

#Actividad 1 

#1 - ¿Qué es GitHub?   

#GitHub es una plataforma en línea que se usa principalmente para almacenar y compartir código de programación. 
#Git es un sistema de control de versiones, lo que significa que puedes llevar un registro de los cambios realizados en el código a lo largo del tiempo. Además, GitHub permite que varios programadores colaboren en el mismo proyecto, se comuniquen a través de comentarios y gestionen tareas. 

#2 - ¿Cómo crear un repositorio en GitHub? 

#Yendo a la página principal de GitHub en la esquina superior derecha hay un simbolo “+” donde ahí figura para poder hacer un nuevo repositorio. 

#3 - ¿Cómo crear una rama en Git? 

#Con el comando “Git branch nueva-rama" (Es un ejemplo, se tiene que cambiar el nombre de la rama al que uno necesite el original es git branch –el nombre de la rama que quieran-) 

#4 - ¿Cómo cambiar a una rama en Git? 

#Con el comando git checkout –nombre de la rama- con el ejemplo antes dado sería: git checkout nueva-rama 

#5 – ¿Cómo fusionar ramas en Git? 

#En mi caso si quiero fusionar “nueva-rama” a la master sería, git merge nueva-rama lo que fusionaria la rama “nueva-rama” con la master. 

#6 - ¿Cómo crear un commit en Git? 

#on el comando git commit luego de añadir lo necesario bastaría. Se le podría agregar un mensaje cambiando un poco el comando por ejemplo: git commit –m “Cambios hechos en la rama master” así aparecería ese mensaje en el commit. 

#7 - ¿Cómo enviar un commit a GitHub? 

#Con el comando git push master debería bastar 

#8 - ¿Qué es un repositorio remoto?  

#Un repositorio remoto es una versión de tu repositorio que está alojada en un servidor en línea, como GitHub, permite que varios usuarios colaboren en el mismo proyecto, ya que los cambios se pueden subir y descargar desde cualquier lugar. 

#9 - ¿Cómo agregar un repositorio remoto a Git? 

#Con el comando git remote add seguido del nombre y la URL del repositorio ya se tendría el repositorio en Git. 

#10 - ¿Cómo empujar cambios a un repositorio remoto? 

#Con el comando git push origin –nombre de la rama- estaría hecho. 

#11 - ¿Cómo tirar de cambios de un repositorio remoto? 

#Con el comando git pull origin –nombre de la rama- debería estar hecho.  

#12 - ¿Qué es un fork de repositorio? 

#Un fork de repositorio es una copia de un repositorio que se crea en tu cuenta de GitHub. Esto te permite hacer cambios en el código sin afectar el repositorio original. 

#13 - ¿Cómo crear un fork de un repositorio? 

#Estando en el repositorio deseado, en la esquina superior derecha debería aparecer un boton llamado Fork, apretandolo te llevaría a opciones de Fork donde se le puede agregar una descripción e incluso cambiar el nombre principal. Una vez hecho ya tendría la copia o Fork del repositorio deseado. 

#14 - ¿Cómo enviar una solicitud de extracción (pull request) a un repositorio? 

#Haz clic en el botón "Pull request": En la página de tu fork, haz clic en el botón verde "New Pull Request". 

#Selecciona la rama y el repositorio de destino: En la pantalla de pull request, selecciona la rama de tu fork y la rama del repositorio original a la que deseas enviar los cambios. 

#Escribe un mensaje y descripción: Explica los cambios que has hecho y por qué deberían ser aceptados. 

#Haz clic en "Create Pull Request": Una vez que hayas completado el mensaje, haz clic en el botón para crear la solicitud. 

 

#15 – ¿Cómo aceptar una solicitud de extracción? 

 

#En la sección de “Pull Request” apareceran las solicitudes de extracción, una vez seleccionada una se clickea en la opción  “Merge pull request”, luego “Confirm Merge” y ahí debería estar hecho. 

 

#16 - ¿Qué es una etiqueta en Git? 

 

#Una etiqueta en Git es una referencia a un punto específico en el historial del repositorio, normalmente utilizada para marcar versiones importantes, como una nueva versión del software. 

#17 - ¿Cómo crear una etiqueta en Git? 

#Con el comando git tag –nombre de etiqueta- debería estar creada. 

#18 - ¿Cómo enviar una etiqueta a GitHub? 

#Una vez creada la etiqueta con el comando git push origin –nombre de la etiqueta- debería estar hecho. 

#19 - ¿Qué es un historial de Git? 

#El historial de Git es una secuencia de registros que muestra todos los cambios (commits) realizados en un repositorio. Cada commit representa un conjunto de cambios en el código, junto con información sobre quién lo hizo, cuándo y por qué. 

#20 - ¿Cómo ver el historial de Git?  

#Con el comando git log debería de poder verse todo el historial de commits. 

#21 - ¿Cómo buscar en el historial de Git? 

#Con el comando anteriormente mencionado (git log) y lo que desee, aqui se 	varia mucho más el comando ya que se pueden buscar cosas más especificas. 	Por ejemplo, para ver una palabra clave sería: git log --grep= “palabra-clave”. 

#22 - ¿Cómo borrar el historial de Git? 

#Hay diversas maneras de borrar el historial concretamente de Git, pero para 	hacer una eliminación total de historial es con el comando rm –rf .git. 

#23 - ¿Qué es un repositorio privado en GitHub? 

#Un repositorio privado en GitHub es un repositorio cuyo contenido no es		accesible públicamente. Solo las personas que tengan permisos explícitos 		pueden ver, clonar, o contribuir al repositorio. 

#24 - ¿Cómo crear un repositorio privado en GitHub? 

#Estando en la página principal de GutHub, en la esquina superior derecha hay 	un simbolo “+” ahí se clickea en New Reposity. Luego de ingresar a la creación 	de un nuevo repositorio hay diversas configuraciones pero buscamos la de 		“Private” una vez marcada esta opción ya estaría hecho el repositorio en 		privado. 

#25 - ¿Cómo invitar a alguien a un repositorio privado en GitHub? 

#En la configuración del repositorio se busca la opción Access luego Manage 	Access, después click en Invite a collaborator, luego aparece un menu donde 	tiene que buscar el nombre de usuario del colaborador con el que quiera 		trabajar luego de encontrarlo selecciona Add, con eso le llegaría al colaborador 	la invitación y luego debe confirmarla para poder acceder al repositorio. 

#26 - ¿Qué es un repositorio público en GitHub? 

#Un repositorio público en GitHub es un repositorio cuyo contenido es accesible 	para cualquier persona, sin necesidad de invitación o permisos especiales. 		Cualquier usuario puede ver, clonar, bifurcar o contribuir al repositorio, lo que lo 	hace ideal para proyectos de código abierto, compartir recursos, o cualquier 	otro propósito en el que desees que tu trabajo esté disponible públicamente. 

#27 - ¿Cómo crear un repositorio público en GitHub? 

#Para crear un repositorio público en GitHub se debe ir al inicio de la página de 	GitHub luego a la esquina superior derecha donde aparece el simbolo “+” luego 	de ello “New Reposity”. Con estos pasos hechos deberíamos estar en el 		apartado de configuraciones del repositorio, en esta sección nos fijamos que no 	este la opción de Private marcada y una vez visto esto hacer click en Create 	Repository. Con esto hecho debería estar hecho publicamente el repositorio. 

#28 - ¿Cómo compartir un repositorio público en GitHub? 

#Es muy sencillo, con copiar y pegar el URL del repositorio que desea compartir 	ya debería estar hecho. 

#Actividad 2 

#https://github.com/Tomy-Magda/TP2 

#Actividad 3 

#https://github.com/Tomy-Magda/conflict-exercise 