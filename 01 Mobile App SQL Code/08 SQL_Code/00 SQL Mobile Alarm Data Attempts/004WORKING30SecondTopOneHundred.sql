WITH CTE AS (
    SELECT
        alarm_events.eventtime,
        FORMAT(alarm_events.eventtime, 'yyyy-MM-dd HH:mm:ss') AS [Time],
        SUBSTRING(alarm_events.source, CHARINDEX(':/alm:', alarm_events.source) + 6, LEN(alarm_events.source)) AS [Alarm],
        LAG(alarm_events.eventtime) OVER (
            PARTITION BY 
                SUBSTRING(alarm_events.source, CHARINDEX(':/alm:', alarm_events.source) + 6, LEN(alarm_events.source))
            ORDER BY 
                alarm_events.eventtime
        ) AS prev_eventtime
    FROM 
        alarm_events
)
SELECT TOP 100 
    [Time], 
    [Alarm]
FROM 
    CTE
WHERE 
    prev_eventtime IS NULL 
    OR DATEDIFF(SECOND, prev_eventtime, eventtime) > 30
ORDER BY 
    [Time] DESC;
