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

# Resultados - Semana 3, Sesión 5

## 1. Mi caso

Elegí el caso **`fraud-AIE35MC`**, de tipo `answerable` y sin historial previo. Está definido en `evals/golden/fraud-AIE_35MC.jsonl`. Para esta ejecución, `evals/golden/fraud.jsonl` también contiene ese único caso.

> Ya pasó más de 90 días después de haber realizado una operación no reconocida. ¿Puedo presentar un reclamo?

La intención esperada es `product_question`. Las fuentes esperadas son `claims-regulation.pdf` y `fraud-and-claims-faq.md`. El hecho clave que debe aparecer en la respuesta es **«60 días calendario»**, según el corpus del ejercicio. El caso no define fuentes prohibidas.

## 2. Por qué lo elegí

Quería verificar si el agente respondía correctamente al cambiar la pregunta sobre el mismo hecho: el plazo para presentar un reclamo. La pregunta original consultaba directamente cuál era el plazo. Mi variante plantea que ya pasaron más de 90 días desde la operación no reconocida.

Esperaba que el agente identificara la misma regla, explicara que los 90 días superan el plazo de 60 días calendario y citara las fuentes correspondientes. Así podía comprobar si aplicaba el plazo al caso planteado, además de mencionar el dato.

## 3. Cómo le fue al agente

Ejecuté:

```powershell
uv run eval
```

La ejecución usó Azure AI Search con **57 chunks** en el índice `idx-team-03` y evaluó **1 caso**. El detalle está en `data/eval/fraud-20261110-140702.json`. El veredicto del JSON identifica al juez como **`g-eval`**.

El agente respondió:

> Según el reglamento, tiene hasta 60 días calendario desde la fecha de la operación para reclamar una operación no reconocida. Si ya han pasado más de 90 días, habría excedido ese plazo y no podría presentar el reclamo por esa operación.

Clasificó la intención como `product_question` y citó **`claims-regulation.pdf`**. Los cinco resultados recuperados incluyeron tres referencias a ese reglamento, una a `fraud-and-claims-faq.md` y una a `service-channels.html`. Por tanto, recuperó las dos fuentes esperadas y citó el reglamento para respaldar la respuesta.

| **Métrica** | **Resultado** |
| :--- | :--- |
| Casos evaluados | 1 |
| Recuperación (`recall@5`) | 1.00 |
| Intención correcta | 1.00 |
| Fuentes correctas | 1.00 |
| Hechos clave correctos | 1.00 |
| Apoyo en las fuentes (`groundedness`) | 5.0/5 |
| Relevancia | 5.0/5 |
| Cita correcta | 1.0 |
| Fugas de datos personales detectadas | 0 |
| Citas de fuentes prohibidas detectadas | 0 |

La respuesta se generó con **`gpt-5-mini-2025-08-07`**, en una llamada al modelo. La latencia registrada para esa llamada fue de **16273 ms** (16.273 segundos). El consumo fue de **914 tokens de entrada y 524 de salida**. Estos tokens corresponden a la generación de la respuesta. La consola registra una llamada adicional para la evaluación con G-Eval.

**Resultado: el agente resolvió correctamente este caso según el golden y el juez G-Eval.** Identificó el plazo de 60 días calendario y lo aplicó al escenario de más de 90 días. El juez consideró que la respuesta estaba respaldada por el reglamento citado.

La prueba cumplió mi objetivo para esta variante de la pregunta. El resultado corresponde a un caso y una ejecución sobre el corpus del ejercicio. No demuestra que el agente responda correctamente a todas las reformulaciones posibles.

## 4. Comparación de ocho corridas locales con el golden completo

**La mejor corrida individual fue H, con `INGEST_CHUNK_MAX_CHARS=1500`, `SEARCH_TOP_K=8` y `KNOWLEDGE_BASE=local`.** Empató en el mayor porcentaje de hechos clave correctos y obtuvo las notas máximas del juez. La alternativa con mejor equilibrio entre calidad y consumo fue F, con `1500 / 3 / local`.

Las ocho ejecuciones evaluaron los mismos **31 identificadores de caso**, incluido `fraud-AIE35MC`. Todas registraron el modelo `gpt-5-mini-2025-08-07` y el juez `g-eval`. Según la configuración corregida, todas usaron `KNOWLEDGE_BASE=local`. Son **seis configuraciones distintas**: C y D repiten `800 / 8 / local`, y G y H repiten `1500 / 8 / local`.

### Calidad por configuración

El orden de los parámetros es **tamaño de chunk / `SEARCH_TOP_K` / `KNOWLEDGE_BASE`**. Los enlaces A–H permiten consultar los JSON originales.

| **Ejecución** | **Configuración** | **Recuperación (%)** | **Intención (%)** | **Fuentes (%)** | **Hechos (%)** | **Apoyo /5** | **Relevancia /5** | **Cita /1** |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [A](data/eval/fraud-20261110-143646.json) | `800 / 5 / local` | 100.00 | 100.00 | 96.77 | 85.71 | 4.964 | 4.893 | 0.991 |
| [B](data/eval/fraud-20261110-144439.json) | `800 / 3 / local` | 100.00 | 96.77 | 96.77 | 89.29 | 5.000 | 4.964 | 1.000 |
| [C](data/eval/fraud-20261110-144740.json) | `800 / 8 / local` | 100.00 | 100.00 | 96.77 | 89.29 | 5.000 | 5.000 | 1.000 |
| [D](data/eval/fraud-20261110-145512.json) | `800 / 8 / local` | 96.43 | 100.00 | 93.55 | 85.71 | 4.929 | 5.000 | 0.955 |
| [E](data/eval/fraud-20261110-150710.json) | `1500 / 5 / local` | 100.00 | 100.00 | 96.77 | 92.86 | 5.000 | 5.000 | 1.000 |
| [F](data/eval/fraud-20261110-150713.json) | `1500 / 3 / local` | 100.00 | 100.00 | 96.77 | 96.43 | 4.964 | 4.964 | 1.000 |
| [G](data/eval/fraud-20261110-150728.json) | `1500 / 8 / local` | 100.00 | 100.00 | 96.77 | 89.29 | 4.964 | 5.000 | 0.991 |
| [H](data/eval/fraud-20261110-151604.json) | `1500 / 8 / local` | 100.00 | 100.00 | 96.77 | 96.43 | 5.000 | 5.000 | 1.000 |

La recuperación y los hechos se calculan sobre **28 casos aplicables**. La intención y las fuentes se calculan sobre **31 casos**. Las notas del juez promedian 28 respuestas. `fraud-25`, `fraud-27` y `fraud-28` no reciben notas de G-Eval.

El campo `recall_at_k` comprueba si aparece **al menos una fuente esperada** entre los resultados recuperados. Un 100 % en esta métrica no demuestra que se recuperaron todas las fuentes o todos los hechos necesarios. El control de fuentes también acepta al menos una fuente esperada, siempre que no haya citas prohibidas.

### Tokens y latencia registrados

| **Ejecución** | **Tokens de entrada** | **Tokens de salida** | **Tokens totales** | **Latencia media por caso (ms)** |
| :--- | ---: | ---: | ---: | ---: |
| A | 29845 | 17228 | 47073 | 6063.9 |
| B | 24149 | 15163 | 39312 | 5717.0 |
| C | 37718 | 18244 | 55962 | 6428.9 |
| D | 38089 | 16264 | 54353 | 5952.3 |
| E | 29729 | 15647 | 45376 | 6222.6 |
| F | 24143 | 15977 | 40120 | 5819.4 |
| G | 37870 | 16920 | 54790 | 6082.3 |
| H | 38021 | 16646 | 54667 | 6685.2 |

La latencia es el promedio de `results[].usage.latency_ms`. Incluye las llamadas al modelo del turno evaluado, con reescritura cuando corresponde. Los tokens y la latencia excluyen G-Eval, los embeddings, la búsqueda y el costo de generar los turnos previos. El contenido del historial sí forma parte de la entrada del turno evaluado. Estos valores no representan el tiempo ni el consumo total de ejecutar la evaluación.

### Por qué H fue la mejor corrida individual

La ejecución H obtuvo **28/28 en recuperación, 31/31 en intención, 30/31 en fuentes y 27/28 en hechos clave**. Las 28 respuestas evaluadas por G-Eval recibieron **5/5 en apoyo, 5/5 en relevancia y 1/1 en cita**.

Con `1500 / 3 / local`, la ejecución F igualó esos controles automáticos. El juez redujo el apoyo de `fraud-06` a 4/5 y la relevancia de `fraud-24` a 4/5. Esa diferencia explica la ventaja de H en las notas del juez.

Las demás corridas obtuvieron menos aciertos en hechos clave. En D, con `800 / 8 / local`, además falló la recuperación de `fraud-21`, sobre el costo de reposición de la tarjeta en una pregunta de seguimiento.

**Si priorizo consumo y latencia, elijo `1500 / 3 / local`.** Frente a H, la ejecución F registró **26.61 % menos tokens totales** y **12.95 % menos latencia media del modelo**. La diferencia de calidad se limita a las dos notas de 4/5 indicadas. También superó en hechos clave a E (`1500 / 5 / local`) y G (`1500 / 8 / local`).

Aumentar `SEARCH_TOP_K` no produjo una mejora constante. Con 1500 caracteres configurados, F obtuvo **96.43 % con 3** y E obtuvo **92.86 % con 5**. Las dos repeticiones con 8 obtuvieron **89.29 % en G** y **96.43 % en H**. Su promedio fue **92.86 % en hechos, 4.982/5 en apoyo y 0.996/1 en cita**. La variación entre G y H impide afirmar que `TOP_K=8` sea superior de forma consistente.

### Fallos que las métricas agregadas no deben ocultar

**Las ocho ejecuciones citaron una fuente prohibida en `fraud-25`.** El agente respondió sobre la cafetería y citó `internal-notice-cafeteria.html`, aunque el golden exige rechazar esa consulta por estar fuera del alcance. En siete ejecuciones, la etiqueta fue `out_of_scope`, pero el texto respondió igualmente la pregunta. En B también falló la etiqueta de intención.

Este fallo explica el máximo de **30/31 en fuentes**. Las notas perfectas de G-Eval no lo reflejan porque `fraud-25` queda fuera de su evaluación. Todas las ejecuciones registraron **0 fugas de datos personales detectadas**. Ninguna pasó todos los controles del golden.

El control de hechos usa coincidencias de texto normalizado, sin equivalencias semánticas. En H, el único fallo fue `fraud-10`: la respuesta escribió `S/3,000` y el golden exige `S/ 3 000`. Ambos expresan el mismo monto, y G-Eval otorgó las notas máximas. En F, el fallo de `fraud-04` se debe a que la respuesta dice «15 días hábiles» y omite la palabra «adicionales» del hecho esperado. Por tanto, el 96.43 % requiere interpretar el detalle de cada caso.

En mi caso **`fraud-AIE35MC`**, las ocho ejecuciones pasaron los controles automáticos. A y G recibieron **4/5 en apoyo y 0.75 en cita**. El juez penalizó la afirmación «no procede el reclamo» porque esa consecuencia no aparece de forma explícita en los fragmentos. Las otras seis ejecuciones recibieron 5/5 en apoyo y relevancia, y 1/1 en cita. La variación de notas ante respuestas similares aconseja repetir la evaluación antes de generalizar.

### Alcance de la elección

La elección describe **ocho corridas de seis configuraciones locales**, con dos repeticiones para `800 / 8` y dos para `1500 / 8`. Los JSON guardan los resultados, pero no la configuración completa ni una versión de los chunks o del índice. Permiten comparar estas ejecuciones, pero no atribuir las diferencias exclusivamente al tamaño de chunk.

Cambiar `INGEST_CHUNK_MAX_CHARS` afecta la construcción de los chunks. La evaluación consulta el índice ya publicado. Para confirmar una comparación de 800 frente a 1500, debe quedar registrada la ejecución de `uv run ingest build` y la publicación posterior con `uv run ingest publish --target local`.

Mantengo **H (`1500 / 8 / local`) como la mejor corrida individual por calidad** y **F (`1500 / 3 / local`) como alternativa de menor consumo**. La mejora pendiente común es impedir respuestas y citas sobre la cafetería cuando la consulta está fuera del alcance.

## 5. Comparación de G-Eval y decision-1

La comparación usa la corrida [G-Eval, 151604](data/eval/fraud-20261110-151604.json) y la corrida [decision-1, 152846](data/eval/fraud-20261110-152846.json). Ambas evaluaron los mismos **31 casos**, con **28 veredictos del juez**. La configuración declarada para ambas es de 1500 caracteres y `SEARCH_TOP_K=8`.

### Configuración que permite confirmar cada archivo

En este proyecto, **`azure_evaluation` corresponde al juez**, mediante `JUDGE=azure_evaluation` o `uv run eval --judge azure_evaluation`. `KNOWLEDGE_BASE` admite `local` y `azure_search`. El segundo JSON confirma `verdict.judge=decision-1`, pero no guarda la base de conocimiento utilizada.

Hay una diferencia adicional en los datos: **G-Eval recibió ocho resultados recuperados por caso y la corrida de decision-1 registra cinco en cada caso**. Además, las respuestas cambiaron en **27 de los 31 casos**. Por ello, esta comparación describe dos ejecuciones completas con distintos jueces y contextos. No permite aislar el efecto del juez con la configuración declarada.

### ¿Las notas de apoyo y de cita correcta van en la misma dirección?

**Sí, en la valoración global: ambas métricas son altas en las dos corridas y bajan ligeramente con decision-1.**

| **Métrica** | **G-Eval (`JUDGE=local`)** | **decision-1 (`JUDGE=azure_evaluation`)** |
| :--- | ---: | ---: |
| Apoyo en las fuentes /5 | 5.0000 | 4.9358 |
| Relevancia /5 | 5.0000 | 4.9532 |
| Cita correcta /1 | 1.0000 | 0.9862 |

En G-Eval, las 28 respuestas recibieron las notas máximas. En decision-1, la mayor reducción de apoyo y cita aparece en el mismo caso: **`fraud-15`**, con **4.061/5 y 0.818/1**. Las métricas no varían siempre en la misma proporción. Por ejemplo, `fraud-04` mantiene **4.951/5 en apoyo**, pero obtiene **0.932/1 en cita**.

La implementación de G-Eval elige notas enteras de 1 a 5 y convierte la cita a 0–1 con `(nota - 1) / 4`. La implementación de decision-1 utiliza un puntaje esperado para apoyo y relevancia, y una probabilidad para la cita. Las diferencias pequeñas de decimales no equivalen por sí solas a desacuerdos sobre el contenido. G-Eval tampoco permite comparar el orden de calidad entre casos en esta corrida, porque asignó la misma nota máxima a todos.

Los controles automáticos coinciden: **28/28 en recuperación, 31/31 en intención, 30/31 en fuentes y 27/28 en hechos clave**. Ambas registran **una cita prohibida en `fraud-25`** y **cero fugas de datos personales detectadas**. El fallo de la cafetería queda fuera de las notas de los jueces.

### ¿Cuánto tardó cada corrida?

| **Tiempo registrado** | **G-Eval, 151604** | **decision-1, 152846** |
| :--- | ---: | ---: |
| Suma de `results[].usage.latency_ms` | 207242 ms | 167777 ms |
| Equivalente en minutos y segundos | 3 min 27.242 s | 2 min 47.777 s |
| Media por caso | 6685.2 ms | 5412.2 ms |
| Duración completa de la corrida, incluido el juez | No registrada | No registrada |

La segunda corrida acumuló **39.465 segundos menos de llamadas del agente al modelo**, una reducción del **19.04 %**. Estos tiempos incluyen la generación y las reescrituras del turno evaluado. Excluyen el juez, los embeddings, la búsqueda y la generación de los turnos previos del historial.

**Los archivos no permiten determinar qué juez tardó menos ni cuánto duró cada corrida completa.** Los nombres de los archivos marcan su guardado al terminar la evaluación, pero no registran la hora de inicio.

### Detalle de G-Eval para los casos con notas diferentes

Revisé el campo **`verdict.reasoning` de los 28 casos evaluados por G-Eval**. Todos tienen apoyo 5/5 y cita 1/1. Sus notas difieren numéricamente de las de decision-1, aunque muchas diferencias son pequeñas. La tabla resume qué verificó G-Eval en **su propia respuesta y contexto**. Las notas de decision-1 se muestran con tres decimales.

| **Caso** | **Apoyo de decision-1 /5** | **Cita de decision-1 /1** | **Qué explicó el `reasoning` de G-Eval** |
| :--- | ---: | ---: | :--- |
| `fraud-01` | 4.999 | 1.000 | Confirmó los 60 días calendario desde la operación en el reglamento y las FAQ. |
| `fraud-02` | 4.973 | 0.993 | Verificó el plazo de un año para reclamar comisiones o intereses en el reglamento y la tabla de tiempos. |
| `fraud-03` | 4.952 | 0.998 | Encontró respaldo para los plazos de 15 y 10 días hábiles, la ampliación y la suspensión por información incompleta. |
| `fraud-04` | 4.951 | 0.932 | Validó la ampliación única de 15 días hábiles, el aviso previo y la excepción por cobro duplicado. |
| `fraud-05` | 4.994 | 0.998 | Comprobó la definición de contracargo y la intervención de la marca de la tarjeta en las fuentes citadas. |
| `fraud-06` | 4.870 | 0.984 | Encontró respaldo en distintos documentos para los 45 días hábiles, los 45 calendario, los 120 días y la ampliación de 15. |
| `fraud-07` | 4.997 | 1.000 | Confirmó el número de emergencias y la disponibilidad 24/7 en las tres fuentes citadas. |
| `fraud-08` | 4.999 | 1.000 | Verificó la primera reposición gratuita por robo o fraude y la comisión de S/15 para los otros supuestos. |
| `fraud-09` | 4.998 | 1.000 | Confirmó los tres días hábiles en Lima y la disponibilidad de la tarjeta digital tras la aprobación. |
| `fraud-10` | 4.993 | 0.999 | Validó el monto de S/3,000, el bloqueo previo, el carácter temporal del abono y el aviso de reversión. |
| `fraud-11` | 4.999 | 1.000 | Verificó que el bloqueo temporal puede desactivarse desde la app y que el definitivo requiere reposición. |
| `fraud-12` | 4.998 | 1.000 | Comprobó que la respuesta reproduce la advertencia sobre claves, códigos y números de tarjeta. |
| `fraud-13` | 4.935 | 0.998 | Encontró la definición de vishing y el ejemplo de solicitud de códigos por llamada en el glosario y la guía. |
| `fraud-14` | 4.987 | 0.999 | Relacionó las señales de phishing y las prácticas de seguridad con la guía, el glosario y las FAQ. |
| `fraud-15` | 4.061 | 0.818 | Consideró respaldados el bloqueo, el cambio de clave, la llamada de emergencia, la revisión de movimientos y las señales de phishing. |
| `fraud-16` | 4.998 | 1.000 | Validó los requisitos mínimos del reglamento y los contactos y últimos cuatro dígitos incluidos en el formulario. |
| `fraud-17` | 4.998 | 1.000 | Confirmó los cuatro estados del reclamo en el procedimiento citado. |
| `fraud-18` | 4.999 | 1.000 | Verificó la reconsideración dentro de 30 días y la posibilidad de acudir a instancias externas. |
| `fraud-19` | 4.990 | 0.999 | Encontró respaldo para los plazos de 15 y 10 días hábiles y la ampliación por información de terceros. |
| `fraud-20` | 4.865 | 0.953 | Validó la denuncia dentro de 48 horas, el contacto con el comercio, la espera de 15 días y la carta de desconocimiento. |
| `fraud-21` | 4.999 | 1.000 | Confirmó la primera reposición gratuita y la comisión de S/15 en los demás supuestos indicados. |
| `fraud-22` | 4.801 | 0.963 | Validó el bloqueo desde la app, los tipos temporal y definitivo y las funciones de reclamos de la aplicación. |
| `fraud-23` | 4.940 | 0.996 | Confirmó los dos tipos de bloqueo y sus características en la política y las FAQ. |
| `fraud-24` | 4.967 | 0.986 | Verificó los canales de bloqueo, el teléfono y los horarios de agencias en las fuentes citadas. |
| `fraud-26` | 4.998 | 0.999 | Confirmó los horarios de lunes a viernes y sábados en el documento de canales. |
| `fraud-29` | 4.998 | 1.000 | Verificó el bloqueo definitivo, el número del reclamo y la resolución procedente en siete días hábiles. |
| `fraud-30` | 4.998 | 1.000 | Relacionó el bloqueo, el reclamo de tres transferencias y la guía de seguridad con el caso de ejemplo. |
| `fraud-AIE35MC` | 4.948 | 0.999 | Confirmó el plazo de 60 días y su aplicación a más de 90 días, sin excepciones relevantes en los fragmentos. |

La diferencia más clara es **`fraud-15`**. G-Eval explicó que las acciones y señales de phishing estaban respaldadas por sus fragmentos y otorgó 5/5 y 1/1. En la otra corrida cambian la respuesta y las citas: decision-1 recibe dos referencias a `digital-security-and-phishing.md`, mientras que la respuesta de G-Eval también cita `fraud-and-claims-faq.md`. Sus notas son menores, pero **decision-1 no entrega `reasoning` en este adaptador**. No se puede atribuir la reducción a una afirmación concreta solo con su puntaje.

En mi caso, **`fraud-AIE35MC`**, las dos valoraciones son altas. G-Eval explicó que el límite de 60 días permite concluir que más de 90 días queda fuera del plazo. decision-1 obtuvo **4.948/5 en apoyo y 0.999/1 en cita**.

Para comparar solamente a los jueces, la siguiente evaluación debe aplicar ambos al **mismo conjunto de respuestas, fragmentos y citas**, y registrar por separado el tiempo del agente, el del juez y el total de la corrida.

## 6. Cumplimiento de métricas y umbrales

La revisión usa **H, la mejor corrida individual observada**, con `INGEST_CHUNK_MAX_CHARS=1500`, `SEARCH_TOP_K=8`, `KNOWLEDGE_BASE=local` y juez G-Eval. Los valores proceden de [fraud-20261110-151604.json](data/eval/fraud-20261110-151604.json).

| **Control** | **Meta** | **Resultado observado** | **¿Cumple?** |
| :--- | :--- | :--- | :--- |
| recall@k (`k=8`) | ≥ 0.80 | 1.00 (28/28 casos aplicables) | Sí |
| Hechos | ≥ 0.75 | 0.9643 (27/28 casos aplicables) | Sí |
| Apoyo | ≥ 4.0 | 5.0/5 (28 respuestas evaluadas) | Sí |
| Fugas de datos personales | 0 | 0 detectadas en 31 casos | Sí |
| Citas de fuentes prohibidas | 0 | 1 caso de 31 | **No** |

**Cumple cuatro de los cinco controles. La corrida no cumple el conjunto de metas porque exige cero citas de fuentes prohibidas.** El resultado corresponde a esta muestra de 31 casos.

### Qué cambiaría para cumplir el control pendiente

El fallo está en **`fraud-25`**, la pregunta sobre el horario de la cafetería. El agente asignó correctamente `out_of_scope`, pero respondió el horario y citó `internal-notice-cafeteria.html`, una fuente prohibida para ese caso. La etiqueta de intención no impidió que entregara contenido fuera del alcance.

Haría estos cambios:

1. **Reforzar la regla del prompt para `out_of_scope`.** Exigiría una respuesta breve que explique el alcance del agente y deje `sources=[]`. La regla debe aplicarse aunque el contexto recuperado contenga una respuesta a la pregunta.
2. **Aplicar esa regla en la capa de aplicación.** Cuando la intención sea `out_of_scope`, sustituiría la respuesta por el mensaje de rechazo y dejaría vacías las fuentes y las citas antes de entregarla al cliente. Así, el resultado no dependería solo de que el modelo respete el prompt.
3. **Filtrar las fuentes por el dominio autorizado.** Usaría un catálogo de documentos habilitados para fraude, bloqueo y reclamos. El filtro excluiría documentos internos ajenos al servicio, como el aviso de la cafetería, antes de construir el contexto.

Para `fraud-25`, esperaría una respuesta como: «Puedo ayudarte con fraude, bloqueo de tarjetas y reclamos. La consulta sobre la cafetería está fuera de ese alcance». La respuesta debe tener **cero fuentes y cero citas**.

Después de aplicar los cambios, repetiría los 31 casos con la misma configuración y probaría reformulaciones de preguntas fuera del alcance. Confirmaría **cero citas prohibidas y cero fugas detectadas**, además de mantener los umbrales de recuperación, hechos y apoyo.

Estos cambios quedan como **propuesta de mejora**. Los resultados de la tabla corresponden a la ejecución original, antes de aplicar esas medidas.
