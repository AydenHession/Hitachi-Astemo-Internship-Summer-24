WITH CTE AS (
    SELECT
        alarm_events.eventtime,
        CONVERT(VARCHAR, alarm_events.eventtime, 101) + ' ' + 
        RIGHT('0' + CAST(CASE WHEN DATEPART(HOUR, alarm_events.eventtime) % 12 = 0 THEN 12 ELSE DATEPART(HOUR, alarm_events.eventtime) % 12 END AS VARCHAR), 2) + ':' + 
        RIGHT('0' + CAST(DATEPART(MINUTE, alarm_events.eventtime) AS VARCHAR), 2) + ':' + 
        RIGHT('0' + CAST(DATEPART(SECOND, alarm_events.eventtime) AS VARCHAR), 2) + ' ' + 
        CASE WHEN DATEPART(HOUR, alarm_events.eventtime) < 12 THEN 'AM' ELSE 'PM' END AS [FormattedTime],
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
    [FormattedTime] AS [Time], 
    [Alarm]
FROM 
    CTE
WHERE 
    prev_eventtime IS NULL 
    OR DATEDIFF(SECOND, prev_eventtime, eventtime) > 30
ORDER BY 
    eventtime DESC;
