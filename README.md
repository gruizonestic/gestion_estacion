# Estación de Massanasa

_Proyecto de gestión automatica de la infraestructura IT de la estación de Massanasa_

## Comenzando 🚀

_Se nos ha solicitado un proyecto piloto en el que tener un despliegue de todos los sistemas que utiliza la estación_

### Pre-requisitos 📋

```
Docker version 20.10.21
Docker-Compose 1.29.2
```

### Instalación 🔧

_Proceso para poder lanzar en local el despliegue de contenedores_

```
cd gestion_estacion
docker-compose up
```

_Para finalizar los servicios_

```
docker-compose down
```
## Configuración FTP
Usuario y contraseña del servicio FTP:
```
Usuario: user
Contraseña: passpass1234
```

## Autores

* **Guillermo Ruiz** - [gruisonestic](https://github.com/gruizonestic)
* **Guillermo Navio** - [guillermo-navio](https://github.com/guillermo-navio)
* **Jordi Ros** - [jorosmayor](https://github.com/jorosmayor)

## Diagrama
```mermaid
   flowchart LR
   %% Grafo de la orquestación de los puntos de venta
    subgraph puntos_de_venta
        direction LR
        %% Grafo del despliegue que tenemos para los terminales automáticos
        subgraph Terminal_automática
            direction LR
            %% Cada uno de los terminales se compone de dos contenedores, uno se encarga de gestionar la TPV y el otro de gestionar la interfaz de productos
            subgraph Terminal_1
                terminalAutoPagos1(TPV 1: C)<-->terminalAutoFrontal1(Frontend 1: Java y JavaFX)
            end
            subgraph Terminal_2
                terminalAutoPagos2(TPV 2: C)<-->terminalAutoFrontal2(Frontend 2: Java y JavaFX)
            end
            subgraph Terminal_3
                terminalAutoPagos3(TPV 3: C)<-->terminalAutoFrontal3(Frontend 3: Java y JavaFX)
            end
            subgraph Terminal_4
                terminalAutoPagos4(TPV 4: C)<-->terminalAutoFrontal4(Frontend 4: Java y JavaFX)
            end
        end
        subgraph Terminal_manual
            direction LR
            %% Cada uno de los terminales tiene la interfaz de productos que será gestionada por los empleados de la estación
            terminalManual1(Frontend_1: Java y JavaFX)
            terminalManual2(Frontend_2: Java y JavaFX)
        end
        Terminal_automática <--> backend_ventas
        Terminal_manual <--> backend_ventas
        subgraph backend_ventas
            direction LR
            %% Los Backs se encargan de 
            backendGestion1(Backend_1: Java)
            backendGestion2(Backend_2: Java)
            backendGestion3(Backend_3: Java)
        end
        backend_ventas <--> BBDD_Pagos
        subgraph BBDD_Pagos
            bbddPagos1[(BBDD_pagos)] --> bbddPagos2[(BBDD_pagos_esclavo)]
        end
        BBDD_Pagos <-->realizar_pagos
        subgraph realizar_pagos
            backendPagos(Backend: Python) 
        end
    end
    backend_ventas<-->apis
    backend_puertas<-->apis

    %% Grafo de la conexión con las API
    subgraph apis
        direction LR
        api_1(API_empresa1: API REST)
        api_2(API_empresa2: API SOAP)
        api_3(API_empresa3: JSON)
        api_4(API_empresa5: XML)
    end
        api_1<-->empresa_1([Servicio Empresa 1])
        api_2<-->empresa_2([Servicio Empresa 2])
        api_3<-->empresa_3([Servicio Empresa 3])
        api_4<-->empresa_4([Servicio Empresa 4])

    %% Grafo de la gestión de las puertas de acceso
    subgraph puertas_acceso
        direction LR
        subgraph frontales_puertas_acceso
            direction LR
            puerta_acceso1(Puerta_1: Python)
            puerta_acceso2(Puerta_2: Python)
            puerta_acceso3(Puerta_3: Python)
            puerta_acceso4(Puerta_4: Python)
            puerta_acceso5(Puerta_5: Python)
            puerta_acceso6(Puerta_6: Python)
        end
        frontales_puertas_acceso <--> backend_puertas
        subgraph backend_puertas
            direction LR
            back_puertas1(Backend_1: GO)
            back_puertas2(Backend_2: GO)
            back_puertas3(Backend_3: GO)
        end
    end

    %%Grafo de la gestión de la domótica
    subgraph servicios_propios
        direction LR
        subgraph terminales_fichaje
            direction LR
            terminal_fichaje1(Fichaje_1: Python)
            terminal_fichaje2(Fichaje_2: Python)
        end
        subgraph BBDD_Fichajes
            bbdd_fichaje1[(BBDD_fichajes)] --> bbdd_fichaje2[(BBDD_fichajes_Esclavo)]
        end
        terminales_fichaje --> bbdd_fichaje1
        backend_estacion(Backend 1: Python)-->gestor_luces(API Luces)
        backend_estacion-->gestor_puertas(API Puertas)
    end
    gestor_luces-->servicio_luces(Servicio Luces)
    gestor_puertas-->servicio_puertas(Servicio Puertas)

    %%Grafo de los monitores de los horarios
    subgraph horarios
        balanceador_monitores(Balanceador: HA Proxy)
        balanceador_monitores <--> frontales_monitores
        subgraph frontales_monitores
            direction LR
            frontal_monitor1(Frontend_1: Angular)
            frontal_monitor2(Frontend_2: Angular)
        end
        frontales_monitores <--> backend_monitores
        subgraph backend_monitores
            direction LR
            backend_monitor1(Backend 1: Node)
            backend_monitor2(Backend 2: Node)
        end
        backend_monitores<-->apigestora(API Gestora Trenes)
    end
    apigestora<-->gestora([Servicio Gestora Trenes])
```
