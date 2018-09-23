### Verificar si ha estado dentro de la etapa finalista
import re

valid_finalist = lambda p: 1 if re.search(r"(finalista|seleccionado|terna)", p['postulacion_nombre_categoria'], re.I) and not re.search(r"(?=.*(finalista|seleccionado|terna))(?=.*(sin|no|pre))", p['postulacion_nombre_categoria'], re.I) else 0

df_applicants['flg_finalista'] = df_applicants.apply(valid_finalist, axis=1)
df_applicants

df_finalista = df_applicants.groupby('flg_finalista').size().reset_index(name='counts')
df_finalista['porcentaje'] = (df_finalista['counts']/df_finalista['counts'].sum())*100
df_finalista