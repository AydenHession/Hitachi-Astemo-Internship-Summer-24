WITH CTE AS (
    SELECT
        alarm_events.eventtime,
        FORMAT(alarm_events.eventtime, 'yyyy-MM-dd HH:mm:ss') AS [Time],
        SUBSTRING(alarm_events.source, CHARINDEX(':/alm:', alarm_events.source) + 6, LEN(alarm_events.source)) AS [Alarm],
        ROW_NUMBER() OVER (
            PARTITION BY 
                SUBSTRING(alarm_events.source, CHARINDEX(':/alm:', alarm_events.source) + 6, LEN(alarm_events.source))
            ORDER BY 
                alarm_events.eventtime DESC
        ) AS rn,
        LAG(alarm_events.eventtime) OVER (
            PARTITION BY 
                SUBSTRING(alarm_events.source, CHARINDEX(':/alm:', alarm_events.source) + 6, LEN(alarm_events.source))
            ORDER BY 
                alarm_events.eventtime DESC
        ) AS prev_eventtime
    FROM 
        alarm_events
),
FilteredCTE AS (
    SELECT
        [Time],
        [Alarm],
        rn,
        prev_eventtime,
        eventtime
    FROM 
        CTE
    WHERE 
        rn = 1 OR 
        DATEDIFF(SECOND, prev_eventtime, eventtime) > 30
)
SELECT TOP 100 
    [Time], 
    [Alarm]
FROM 
    FilteredCTE
ORDER BY 
    [Time] DESC;
