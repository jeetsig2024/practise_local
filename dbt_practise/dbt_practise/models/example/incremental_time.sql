{{config(materialized='incremental',unique_key='t_time')}}

select t.*  from "SNOWFLAKE_SAMPLE_DATA"."TPCDS_SF10TCL"."TIME_DIM" t
where to_time(concat(T_HOUR::varchar, ':', T_MINUTE, ':', T_SECOND)) <= current_time

{% if is_incremental() %}
   and t_time>=(select max(t_time) from {{this}})
{% endif %}