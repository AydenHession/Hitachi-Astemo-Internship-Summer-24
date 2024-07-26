WITH CTE AS (
    SELECT
        FORMAT(alarm_events.eventtime, 'yyyy-MM-dd HH:mm:ss') AS [Time],
        SUBSTRING(alarm_events.source, CHARINDEX(':/alm:', alarm_events.source) + 6, LEN(alarm_events.source)) AS [Alarm],
        ROW_NUMBER() OVER (PARTITION BY FORMAT(alarm_events.eventtime, 'yyyy-MM-dd HH:mm:ss'), SUBSTRING(alarm_events.source, CHARINDEX(':/alm:', alarm_events.source) + 6, LEN(alarm_events.source))
                          ORDER BY alarm_events.eventtime DESC) AS rn
    FROM alarm_events
)
SELECT TOP 100 [Time], [Alarm]
FROM CTE
WHERE rn = 1
ORDER BY [Time] DESC;
