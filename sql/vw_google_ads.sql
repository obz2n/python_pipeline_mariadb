CREATE OR REPLACE VIEW vw_google_ads AS
SELECT
  `Ad_ID` AS ad_id,
  CASE `Campaign_Name`
    WHEN 'machnelearningbasics'     THEN 'Machine Learning Basics'
    WHEN 'webdevmastery'            THEN 'Web Dev Mastery'
    WHEN 'sqldatabsetraining'       THEN 'SQL Database Training'
    WHEN 'cloudcomputngcourse'      THEN 'Cloud Computing Course'
    WHEN 'aimarketing'              THEN 'AI Marketing'
    WHEN 'datasciencebootcamp'      THEN 'Data Science Bootcamp'
    WHEN 'businessanlyticsclass'    THEN 'Business Analytics Class'
    WHEN 'cybersecurtyfundamentals' THEN 'Cybersecurity Fundamentals'
    WHEN 'python4data'              THEN 'Python for Data'
    WHEN 'deeplearnngpro'           THEN 'Deep Learning Pro'
  END AS campanha,
  CASE
    WHEN DAY(`Ad_Date`) = 11 AND MONTH(`Ad_Date`) <> 11
    THEN STR_TO_DATE(
           CONCAT(YEAR(`Ad_Date`), '-', DAY(`Ad_Date`), '-', MONTH(`Ad_Date`)),
           '%Y-%m-%d')
    ELSE DATE(`Ad_Date`)
  END AS data_anuncio,
  CASE WHEN `Location` = 'New Delhi' THEN 'Delhi' ELSE `Location` END AS cidade,
  `Device`  AS dispositivo,
  `Keyword` AS keyword,
  CAST(NULLIF(TRIM(`Clicks`), '')      AS DECIMAL(12,0)) AS cliques,
  CAST(NULLIF(TRIM(`Impressions`), '') AS DECIMAL(12,0)) AS impressoes,
  CAST(NULLIF(TRIM(`Cost`), '')        AS DECIMAL(14,2)) AS custo,
  CAST(NULLIF(TRIM(`Leads`), '')       AS DECIMAL(12,0)) AS leads,
  CAST(NULLIF(TRIM(`Conversions`), '') AS DECIMAL(12,0)) AS conversoes,
  CAST(NULLIF(TRIM(`Sale_Amount`), '') AS DECIMAL(14,2)) AS receita
FROM stg_google_ads;