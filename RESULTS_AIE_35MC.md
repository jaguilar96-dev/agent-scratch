# Resultados - Semana 1, Sesión 2

| **Mensaje** | **Intención** | **latency_ms** | **prompt_tokens** | **completion_tokens** | **FOUNDRY_DEPLOYMENT** | **MAX_TURNS** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Hola, buenos días. | greeting | 2456 | 382 | 112 | gpt-5-mini | 10 |
| ¿Cuál es el plazo para presentar un reclamo por una operación que no reconozco? | product_question | 6682 | 441 | 892 | gpt-5-mini | 10 |
| Quiero ver mis movimientos de ayer. | data_query | 6599 | 565 | 846 | gpt-5-mini | 10 |
| Me robaron la tarjeta, bloquéala. | sensitive_action | 8297 | 710 | 907 | gpt-5-mini | 10 |
| ¿Qué necesito para solicitar un préstamo de S/ 20 000? | out_of_scope | 3458 | 853 | 352 | gpt-5-mini | 10 |
| Hola, buenos días. | greeting | 3191 | 382 | 177 | gpt-5-mini | 4 |
| ¿Cuál es el plazo para presentar un reclamo por una operación que no reconozco? | product_question | 7607 | 442 | 891 | gpt-5-mini | 4 |
| Quiero ver mis movimientos de ayer. | data_query | 4652 | 565 | 525 | gpt-5-mini | 4 |
| Me robaron la tarjeta, bloquéala. | sensitive_action | 6449 | 709 | 808 | gpt-5-mini | 4 |
| ¿Qué necesito para solicitar un préstamo de S/ 20 000? | out_of_scope | 3590 | 882 | 297 | gpt-5-mini | 4 |
| Hola, buenos días. | greeting | 4492 | 382 | 363 | gpt-5-nano | 10 |
| ¿Cuál es el plazo para presentar un reclamo por una operación que no reconozco? | product_question | 5880 | 436 | 1044 | gpt-5-nano | 10 |
| Quiero ver mis movimientos de ayer. | data_query | 4757 | 520 | 865 | gpt-5-nano | 10 |
| Me robaron la tarjeta, bloquéala. | sensitive_action | 9626 | 617 | 1538 | gpt-5-nano | 10 |
| ¿Qué necesito para solicitar un préstamo de S/ 20 000? | product_question | 8739 | 748 | 1372 | gpt-5-nano | 10 |
| Hola, buenos días. | greeting | 4136 | 382 | 321 | gpt-5-nano | 4 |
| ¿Cuál es el plazo para presentar un reclamo por una operación que no reconozco? | product_question | 6070 | 458 | 998 | gpt-5-nano | 4 |
| Quiero ver mis movimientos de ayer. | data_query | 6437 | 560 | 926 | gpt-5-nano | 4 |
| Me robaron la tarjeta, bloquéala. | sensitive_action | 6582 | 656 | 991 | gpt-5-nano | 4 |
| ¿Qué necesito para solicitar un préstamo de S/ 20 000? | product_question | 9271 | 757 | 1661 | gpt-5-nano | 4 |

## 1. ¿`gpt-5-mini` o `gpt-5-nano` para clasificar intención? ¿Qué pasa con la latencia y la calidad?

En estas mediciones, `gpt-5-mini` conviene si la prioridad es reducir la latencia. La latencia media fue 5298.1 ms con `gpt-5-mini` y 6599.0 ms con `gpt-5-nano`. `gpt-5-nano` tardó un 24.6 % más en promedio. `gpt-5-mini` no fue más rápido en todos los mensajes.

Ambos modelos asignaron la misma intención a cuatro de los cinco mensajes distintos. Cada modelo mantuvo sus etiquetas con ambas configuraciones de `MAX_TURNS`. La pregunta sobre el préstamo recibió etiquetas distintas. `gpt-5-mini` devolvió `out_of_scope` y `gpt-5-nano` devolvió `product_question`.

La tabla no incluye las etiquetas esperadas ni define el alcance del agente. Por ello, no permite determinar cuál etiqueta del préstamo es correcta. Tampoco permite calcular porcentajes de acierto.

`gpt-5-nano` registró 1007.9 tokens de salida por mensaje en promedio. `gpt-5-mini` registró 580.7 tokens de salida por mensaje en promedio. La tabla no incluye tarifas para comparar los costos.

Cada mensaje tiene una sola medición por configuración. Los resultados describen esta muestra y no demuestran una ventaja general.

## 2. ¿Cuánto cuesta por mes un `MAX_TURNS=10` frente a un `MAX_TURNS=4`, con el tráfico esperado?

No es posible calcular el costo mensual con los datos de la tabla. Faltan el tráfico mensual y las tarifas de entrada y salida de cada modelo.

Para los mismos cinco mensajes, `gpt-5-mini` registró 6060 tokens totales con `MAX_TURNS=10` y 5678 con `MAX_TURNS=4`. La diferencia fue 382 tokens, una reducción del 6.3 %. `gpt-5-nano` registró 7885 tokens totales con `MAX_TURNS=10` y 7710 con `MAX_TURNS=4`. La diferencia fue 175 tokens, una reducción del 2.2 %.

Los tokens de salida disminuyeron con `MAX_TURNS=4`. En `gpt-5-mini`, la entrada subió de 2951 a 2980 tokens. La salida bajó de 3109 a 2698 tokens. En `gpt-5-nano`, la entrada subió de 2703 a 2813 tokens. La salida bajó de 5182 a 4897 tokens.

Estas reducciones de tokens no indican porcentajes de ahorro monetario. Los resultados tampoco demuestran que recortar el historial cause ese ahorro. La tabla no registra las sesiones, el historial enviado ni las repeticiones controladas.

El cálculo requiere el tráfico mensual y las tarifas por millón de tokens. Con esos datos, se puede aplicar esta fórmula:

`costo mensual = mensajes/mes × (entrada media × tarifa de entrada + salida media × tarifa de salida) / 1 000 000`

La estimación requeriría un tráfico con consumo similar al medido.

## 3. ¿Conviene un modelo chico para `greeting` y `out_of_scope`, y uno grande solo para el resto?

Esta muestra no demuestra una ventaja de usar `gpt-5-nano` para `greeting` y `out_of_scope`. En el saludo, la latencia media fue 2823.5 ms con `gpt-5-mini` y 4314.0 ms con `gpt-5-nano`. En la pregunta sobre el préstamo, `gpt-5-mini` registró una latencia media de 3524.0 ms. `gpt-5-nano` registró 9005.0 ms para esa pregunta. `gpt-5-nano` fue más lento en ambos casos.

`gpt-5-mini` clasificó el préstamo como `out_of_scope`. `gpt-5-nano` lo clasificó como `product_question`. Por esa diferencia, los modelos no necesariamente enviarían el mensaje al mismo flujo.

La comparación mixta usa las mediciones de `gpt-5-nano` para el saludo y el préstamo. Para los otros tres mensajes, usa las mediciones de `gpt-5-mini`. La latencia media calculada sería 6961.8 ms con `MAX_TURNS=10`. Con `MAX_TURNS=4`, sería 6423.0 ms. Ambos valores serían aproximadamente un 26 % mayores que con `gpt-5-mini` para todos los mensajes.

Con `MAX_TURNS=10`, los tokens totales subirían de 6060 a 7226. Con `MAX_TURNS=4`, subirían de 5678 a 7061 tokens. Los valores describen una comparación aritmética, no una prueba de un enrutador real.

Sin tarifas, no es posible calcular el costo de esa comparación. La tabla no incluye mediciones de llamadas adicionales para enrutar. La menor latencia observada respalda usar `gpt-5-mini` como referencia para esta muestra.

# Resultados - Semana 2, Sesión 3

| **INGEST_CHUNK_MAX_CHARS** | **Documentos procesados** | **Chunks generados** | **Observación** |
| :--- | ---: | ---: | :--- |
| 250 | 14 | 82 | Fragmentos más específicos; mayor riesgo de separar información relacionada. |
| 1500 | 14 | 57 | Menos fragmentos y más contexto dentro de cada sección. |

## 1. ¿Cuántos chunks salen con `250` y cuántos con `1500`?

La ingesta generó **82 chunks con `250`** y **57 chunks con `1500`**. Un chunk es un fragmento de texto del corpus.

Ambas ejecuciones procesaron los mismos 14 documentos del corpus `fraud` con `uv run ingest build`. Ambos resultados incluyen `chargeback-form.md`. La configuración de 250 caracteres produjo 25 chunks adicionales, un 43.9 % más que la configuración de 1500 caracteres.

El tamaño configurado indica un objetivo de partición. No establece un límite estricto de caracteres para cada chunk. La ingesta añade los títulos de sección a cada chunk. La ingesta conserva unidades como oraciones o filas de tablas. Con 250 caracteres configurados, el chunk más largo observado contiene 379 caracteres.

## 2. ¿Qué se gana con chunks más pequeños?

Los chunks más pequeños tienden a concentrarse en un solo tema. Esta separación puede mejorar la precisión al recuperar contenido para una consulta. También puede reducir el contenido que no responde a la consulta.

En `chargeback-form.md`, la sección «6. Políticas de Resolución y Tiempos (SLA)» generó cuatro chunks con 250:

- Bloqueo preventivo.
- Abono temporal.
- Tiempo de investigación.
- Fallo desfavorable.

Con 1500, los cuatro temas quedaron en un único chunk.

La comparación confirma que los chunks de 250 separan esos temas. No incluye consultas de recuperación para medir una mejora de precisión.

## 3. ¿Qué se pierde con chunks más pequeños?

Los chunks más pequeños conservan menos contexto. Una regla y su excepción pueden quedar en chunks distintos. También puede separarse una condición relacionada con la regla. Recuperar solo uno de esos chunks puede producir una respuesta incompleta.

En `claims-regulation.pdf`, la sección «5. Abono provisional» generó dos chunks con 250. Un chunk explica cuándo se puede otorgar el abono. El otro chunk explica cuándo se revierte el abono por un reclamo no procedente. Con 1500, ambas partes quedaron en un único chunk.

El tamaño de 1500 conserva más contexto dentro de cada sección. La partición también respeta los encabezados del documento. Por eso, 1500 no garantiza reunir una regla y su excepción si pertenecen a secciones distintas.

# Resultados - Semana 2, Sesión 4

Ejecuciones: `uv run python dev/chat.py` con `KNOWLEDGE_BASE=local` y `SEARCH_TOP_K=5`, `2` y `10`. Entre estas tres ejecuciones solo cambia `SEARCH_TOP_K`. Además, se registra una ejecución con `KNOWLEDGE_BASE=azure_search` y `SEARCH_TOP_K=5`. Cada ejecución contiene cinco turnos consecutivos de una misma sesión. Los tiempos se transcriben de la consola en milisegundos.

| **Pregunta** | **Intención** | **Fuentes citadas** | **¿Fuente correcta?** | **Primer texto en (ms)** | **Respuesta completa en (ms)** | **SEARCH_TOP_K** | **KNOWLEDGE_BASE** |
| :--- | :--- | :--- | :--- | ---: | ---: | ---: | :--- |
| ¿Cuál es el plazo para presentar un reclamo? | `product_question` | `claims-regulation.pdf`, sección 3.1 «Plazo para presentar». | Sí. Respalda los 60 días calendario para operaciones no reconocidas y el año para cobros de comisiones o intereses. | 28119 | 28251 | 5 | local |
| ¿y si es por fraude? | `product_question` | `claims-regulation.pdf`, secciones 3.1 y 4 «Plazos de respuesta». `fraud-and-claims-faq.md`, «¿En cuánto tiempo me responden?». | Sí. Respaldan el plazo para reclamar, los plazos de respuesta de 15 y 10 días hábiles y la ampliación indicada. | 11598 | 11841 | 5 | local |
| ¿Qué es un contracargo? | `product_question` | `credit-card-chargebacks.html`, «Plazos del contracargo». `fraud-and-claims-faq.md`, preguntas sobre plazos para reclamar y recibir respuesta. `claims-regulation.pdf`, secciones 4 y 3.1. | No para definir el término. Las citas tratan sobre plazos. El agente afirmó que no había una definición. | 15479 | 15600 | 5 | local |
| ¿Qué decía la política de bloqueo de 2022? | `product_question` | `card-blocking-policy.docx`, «Responsabilidad por operaciones». | Parcial. La fuente respalda el fragmento citado, pero no corresponde a la versión de 2022. El agente indicó que no disponía de esa versión. | 16361 | 16498 | 5 | local |
| ¿A cuánto está el dólar hoy? | `out_of_scope` | Sin fuentes. | No aplica. El agente rechazó la consulta por estar fuera del alcance del servicio. | 7363 | 7491 | 5 | local |
| ¿Cuál es el plazo para presentar un reclamo? | `product_question` | `claims-regulation.pdf`, sección 3.1 «Plazo para presentar». | Sí. Respalda los 60 días calendario para operaciones no reconocidas y el año para cobros de comisiones o intereses. | 14690 | 14836 | 2 | local |
| ¿y si es por fraude? | `product_question` | `claims-regulation.pdf`, sección 3.1 «Plazo para presentar». `fraud-and-claims-faq.md`, «¿Cuánto tiempo tengo para reclamar un cargo?». | Sí. Ambas fuentes respaldan los 60 días calendario desde la fecha de la operación. | 12886 | 13118 | 2 | local |
| ¿Qué es un contracargo? | `product_question` | `claims-regulation.pdf`, sección 3.1 «Plazo para presentar». `fraud-and-claims-faq.md`, «¿Cuánto tiempo tengo para reclamar un cargo?». | No para definir el término. Las citas tratan sobre plazos. El agente se abstuvo porque los fragmentos no contenían la definición. | 13403 | 13554 | 2 | local |
| ¿Qué decía la política de bloqueo de 2022? | `product_question` | `card-blocking-policy.docx`, «Canales de bloqueo» y «Confirmación obligatoria». | No para 2022. Las citas respaldan el contenido de una política vigente desde 2025. El agente lo atribuyó incorrectamente a 2022. | 13789 | 14082 | 2 | local |
| ¿A cuánto está el dólar hoy? | `out_of_scope` | Sin fuentes. | No aplica. El agente rechazó la consulta por estar fuera del alcance del servicio. | 9694 | 9842 | 2 | local |
| ¿Cuál es el plazo para presentar un reclamo? | `product_question` | `claims-regulation.pdf`, sección 3.1 «Plazo para presentar». | Sí. Respalda los 60 días calendario para operaciones no reconocidas y el año para cobros de comisiones o intereses. | 10236 | 10596 | 10 | local |
| ¿y si es por fraude? | `product_question` | `claims-regulation.pdf`, secciones 3.1 y 4 «Plazos de respuesta». `unrecognized-charges-procedure.md`, «Paso 3: registrar el reclamo». | Sí. Respaldan el plazo para reclamar, los plazos de respuesta y el bloqueo definitivo con reposición por robo o clonación. | 12314 | 12585 | 10 | local |
| ¿Qué es un contracargo? | `product_question` | `credit-card-chargebacks.html`, «Qué es un contracargo». | Sí. La sección contiene la definición que dio el agente. | 10191 | 10382 | 10 | local |
| ¿Qué decía la política de bloqueo de 2022? | `product_question` | `card-blocking-policy.docx`, «Tipos de bloqueo» y «Confirmación obligatoria». | Parcial. Las citas respaldan una política vigente desde 2025. El agente reconoce que no dispone de la versión de 2022 y resume la política recuperada. | 14800 | 15100 | 10 | local |
| ¿A cuánto está el dólar hoy? | `out_of_scope` | Sin fuentes. | No aplica. El agente rechazó la consulta por estar fuera del alcance del servicio. | 10685 | 10921 | 10 | local |
| ¿Cuál es el plazo para presentar un reclamo? | `product_question` | `claims-regulation.pdf`, sección 3.1 «Plazo para presentar». | Sí. Respalda los 60 días calendario para operaciones no reconocidas y el año para cobros de comisiones o intereses. | 5009 | 5253 | 5 | azure_search |
| ¿y si es por fraude? | `product_question` | `claims-regulation.pdf`, secciones 3.1 «Plazo para presentar» y 4 «Plazos de respuesta». | Sí. Respaldan los 60 días calendario para reclamar y los plazos de respuesta de 15 y 10 días hábiles. | 14138 | 14367 | 5 | azure_search |
| ¿Qué es un contracargo? | `product_question` | `credit-card-chargebacks.html`, «Plazos del contracargo». | No para definir el término. La cita respalda los plazos mencionados, pero omite la sección con la definición. | 14384 | 14645 | 5 | azure_search |
| ¿Qué decía la política de bloqueo de 2022? | `product_question` | `card-blocking-policy.docx`, «Canales de bloqueo», «Confirmación obligatoria», «Tipos de bloqueo», «Responsabilidad por operaciones» y «Cuándo se bloquea una tarjeta». | No para 2022. Las citas respaldan una política vigente desde 2025. El agente la atribuyó incorrectamente a 2022. | 14308 | 14769 | 5 | azure_search |
| ¿A cuánto está el dólar hoy? | `out_of_scope` | Sin fuentes. | No aplica. El agente rechazó la consulta por estar fuera del alcance del servicio. | 7282 | 7501 | 5 | azure_search |

## Observaciones sobre las fuentes

- **Contracargo (`KNOWLEDGE_BASE=local`, `SEARCH_TOP_K=5` y `2`):** el corpus sí contiene la definición en `credit-card-chargebacks.html`, sección «Qué es un contracargo», y en `fraud-glossary.md`, entrada «Contracargo». En ambas ejecuciones, las citas mostradas omiten esas secciones. Las respuestas evidencian una omisión de recuperación respecto del corpus local.
- **Política de 2022 (`KNOWLEDGE_BASE=local`, `SEARCH_TOP_K=5`):** `card-blocking-policy-2022.md` existe en el corpus. Sus fragmentos tienen `valid_until=2024-12-31` en `data/chunks/fraud.json`. El filtro de búsqueda excluye documentos vencidos. La ausencia de esa versión en los resultados es coherente con el filtro. La abstención evita inventar su contenido, aunque la cita de `card-blocking-policy.docx` no responde la consulta histórica.
- **Política de 2022 (`KNOWLEDGE_BASE=local`, `SEARCH_TOP_K=2`):** los fragmentos citados de `card-blocking-policy.docx` tienen `valid_from=2025-01-01`. El agente atribuyó esa política a 2022. Además, afirmó que la aplicación móvil permitía bloquear tarjetas. Esta afirmación contradice `card-blocking-policy-2022.md`, que indica que la aplicación móvil no permite el bloqueo. Las citas respaldan el texto recuperado, pero no su atribución histórica.
- **Contracargo (`KNOWLEDGE_BASE=local`, `SEARCH_TOP_K=10`):** la cita incluye «Qué es un contracargo» de `credit-card-chargebacks.html`. La respuesta define el término con respaldo del corpus.
- **Política de 2022 (`KNOWLEDGE_BASE=local`, `SEARCH_TOP_K=10`):** el agente reconoce que los fragmentos disponibles no contienen la versión solicitada. Después resume `card-blocking-policy.docx`, vigente desde 2025. Las citas son pertinentes para esa política, pero no documentan lo que decía en 2022. Además, la respuesta abrevia «fraude confirmado» como «fraude» al describir el bloqueo definitivo.

- **Contracargo (`KNOWLEDGE_BASE=azure_search`, `SEARCH_TOP_K=5`):** la única cita corresponde a «Plazos del contracargo». La respuesta sigue sin definir el término, aunque la definición existe en otra sección del mismo documento.
- **Política de 2022 (`KNOWLEDGE_BASE=azure_search`, `SEARCH_TOP_K=5`):** las cinco citas corresponden a `card-blocking-policy.docx`, con `valid_from=2025-01-01`. La respuesta atribuye a 2022 la política vigente y permite el bloqueo desde la aplicación. La versión de 2022 indica que la aplicación móvil no permite bloquear tarjetas. Hay más secciones citadas, pero la atribución histórica es incorrecta.

## 1. Con `SEARCH_TOP_K=2`, ¿falta información en alguna respuesta?

En la ejecución con `KNOWLEDGE_BASE=local`, sí. La omisión principal es la definición de **contracargo**. El agente no la responde, aunque existe en el corpus. Las dos citas recuperadas tratan sobre plazos de reclamo.

En «¿y si es por fraude?», el agente informa correctamente los 60 días calendario para presentar el reclamo. Omite los plazos de respuesta del banco y la posible ampliación que aparecen con `SEARCH_TOP_K=5`. Esto reduce el contexto de la respuesta.

La pregunta sobre **2022** presenta un error adicional: el agente atribuye a ese año una política vigente desde 2025. La fuente histórica existe, pero queda excluida por el filtro de vigencia. El plazo general de reclamo y el rechazo de la consulta sobre el dólar son adecuados.

## 2. Con `SEARCH_TOP_K=10`, ¿cuántos tokens de entrada más cuesta cada turno? ¿Aparecen fuentes que no vienen al caso?

La tabla compara los tokens de entrada registrados en las tres ejecuciones con `KNOWLEDGE_BASE=local`. Las diferencias usan `SEARCH_TOP_K=2` y `SEARCH_TOP_K=5` como referencias.

| **Pregunta** | **Entrada con 2** | **Entrada con 5** | **Entrada con 10** | **Más tokens: 10 frente a 2** | **Más tokens: 10 frente a 5** |
| :--- | ---: | ---: | ---: | ---: | ---: |
| ¿Cuál es el plazo para presentar un reclamo? | 690 | 932 | 1561 | +871 | +629 |
| ¿y si es por fraude? | 909 | 1182 | 1757 | +848 | +575 |
| ¿Qué es un contracargo? | 1009 | 1393 | 2166 | +1157 | +773 |
| ¿Qué decía la política de bloqueo de 2022? | 1131 | 1584 | 2202 | +1071 | +618 |
| ¿A cuánto está el dólar hoy? | 1389 | 1601 | 2403 | +1014 | +802 |
| **Total de cinco turnos** | **5128** | **6692** | **10089** | **+4961** | **+3397** |

Con `10`, el aumento medio es de **992.2 tokens de entrada por turno frente a `2`** y **679.4 frente a `5`**. La entrada total aumenta un **96.7 % frente a `2`** y un **50.8 % frente a `5`**.

Estas diferencias corresponden a la entrada total registrada. El registro no separa los tokens de los fragmentos recuperados de los demás componentes de la entrada. Además, las respuestas previas cambian entre ejecuciones. Por ello, las diferencias no aíslan el efecto de aumentar `SEARCH_TOP_K`.

Las citas mostradas no incluyen documentos ajenos al dominio. Sin embargo, **las fuentes vigentes de bloqueo no responden la consulta histórica de 2022**. El procedimiento de cargos no reconocidos aporta instrucciones de bloqueo relacionadas con fraude, aunque exceden la pregunta sobre el plazo.

Con `10`, la definición de contracargo sí tiene una cita directa y correcta. La consola muestra las fuentes citadas, sin detallar todos los fragmentos enviados al modelo. Por ello, no permite evaluar la pertinencia de todo el contexto recuperado.

## 3. ¿Qué valor elige el equipo y por qué?

El equipo elige **`SEARCH_TOP_K=10` para la evaluación con `KNOWLEDGE_BASE=local`**. Es el único valor probado que permite responder correctamente la definición de contracargo. También recupera fuentes para explicar los plazos y el procedimiento ante fraude. En la consulta histórica, el agente reconoce que los fragmentos no incluyen una versión de 2022.

El equipo acepta el aumento observado de tokens de entrada para obtener esa mayor cobertura. Con `5`, la definición de contracargo también quedó sin responder.

La elección no resuelve la consulta histórica de 2022. El filtro de vigencia sigue excluyendo ese documento. La decisión sobre `SEARCH_TOP_K` se basa en cinco preguntas y una ejecución local por configuración.

## 4. Anota la siguiente comparación: local frente a AI Search

La comparación usa **`SEARCH_TOP_K=5` en ambos motores**. La columna local corresponde a la primera ejecución registrada con ese valor. Los tiempos son los de respuesta completa y se expresan en milisegundos.

| **Pregunta** | **Fuentes en local** | **Fuentes en AI Search** | **¿Mejoró con el reranker?** | **respuesta completa en (local / AI Search)** |
| :--- | :--- | :--- | :--- | :--- |
| ¿Cuál es el plazo para presentar un reclamo? | `claims-regulation.pdf`, sección 3.1 «Plazo para presentar». | `claims-regulation.pdf`, sección 3.1 «Plazo para presentar». | Sin mejora observable de contenido. Mantiene la misma fuente y los mismos plazos correctos. | 28251 ms / 5253 ms |
| ¿y si es por fraude? | `claims-regulation.pdf`, secciones 3.1 y 4. `fraud-and-claims-faq.md`, «¿En cuánto tiempo me responden?». | `claims-regulation.pdf`, secciones 3.1 y 4. | No se observa mejora. Los plazos citados son correctos. AI Search omite la posible ampliación que incluía la respuesta local. | 11841 ms / 14367 ms |
| ¿Qué es un contracargo? | `credit-card-chargebacks.html`, «Plazos del contracargo». `fraud-and-claims-faq.md`, preguntas sobre plazos para reclamar y recibir respuesta. `claims-regulation.pdf`, secciones 4 y 3.1. | `credit-card-chargebacks.html`, «Plazos del contracargo». | No. Reduce las citas a una sección relacionada, pero sigue sin citar la definición ni responderla. | 15600 ms / 14645 ms |
| ¿Qué decía la política de bloqueo de 2022? | `card-blocking-policy.docx`, «Responsabilidad por operaciones». | `card-blocking-policy.docx`, «Canales de bloqueo», «Confirmación obligatoria», «Tipos de bloqueo», «Responsabilidad por operaciones» y «Cuándo se bloquea una tarjeta». | No. La respuesta empeora al atribuir a 2022 la política vigente desde 2025. La ejecución local reconocía que no disponía de la versión de 2022. | 16498 ms / 14769 ms |
| ¿A cuánto está el dólar hoy? | Sin fuentes. | Sin fuentes. | No aplica. Ambas ejecuciones clasifican la consulta como `out_of_scope` y rechazan dar la cotización. | 7491 ms / 7501 ms |

La tabla evalúa la calidad de las respuestas y las citas mostradas. Las diferencias de tiempo se registran por separado. El cambio de motor no permite atribuir las diferencias exclusivamente al reranker. La salida de consola tampoco confirma por sí sola su activación.
