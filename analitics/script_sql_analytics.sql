SELECT count(1) FROM "db"."tb_dados_api_openweathermap" limit 1

show partitions tb_dados_api_openweathermap

SELECT 
weather[1].description as tempo, 
COUNT(*) AS count
FROM tb_dados_api_openweathermap
where dt > TIMESTAMP '2024-05-25 21:39:29'
GROUP BY weather[1].description

SELECT 
MAX(main.temp_max) AS temperatura_maxima, 
MIN(main.temp_min) temperatura_minima,
AVG(main.temp) AS temperatura_media
FROM tb_dados_api_openweathermap;

SELECT 
    DATE_FORMAT(dt, '%H') AS hora, 
    AVG(
	        CASE 
			            WHEN visibility > 10000 THEN 100.0
					            ELSE (visibility / 10000.0) * 100.0 
							        END
								    ) AS visibilidade_media_porcentagem
								FROM tb_dados_api_openweathermap
								GROUP BY DATE_FORMAT(dt, '%H')
								ORDER BY hora;


								SELECT DATE_FORMAT(dt, '%H') AS horas, CAST(AVG(wind.speed) AS DECIMAL(10,2)) AS media_velocidade, CAST(AVG(wind.deg) AS INT) AS media_kilometros_rodado
								FROM tb_dados_api_openweathermap
								GROUP BY DATE_FORMAT(dt, '%H')
								ORDER BY horas;

