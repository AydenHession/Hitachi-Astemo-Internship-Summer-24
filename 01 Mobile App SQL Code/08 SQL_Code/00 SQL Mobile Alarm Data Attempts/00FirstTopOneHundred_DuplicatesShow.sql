SELECT DISTINCT TOP 100
	FORMAT(alarm_events.eventtime, 'yyyy-MM-dd HH:mm:ss') AS [Time],
  	SUBSTRING(alarm_events.source, CHARINDEX(':/alm:', alarm_events.source) + 6, LEN(alarm_events.source)) AS [Alarm]
FROM alarm_events
ORDER BY alarm_events.eventtime DESC;