-- Fee = 5
-- no charge if sum(payments) >= 100 and count(payments) >= 3
-- Historical fee does not appear in transactions table
-- balance = 0 at the beginning of the year
-- transactions amount is never 0
CREATE OR REPLACE VIEW balance AS WITH months AS (
        SELECT TO_CHAR(
                GENERATE_SERIES(
                    '2020-01-01'::date,
                    '2020-12-01'::date,
                    '1 month'
                ),
                'YYYY-MM'
            ) AS month
    ),
    payments AS (
        SELECT TO_CHAR(date, 'YYYY-MM') AS month,
            amount
        FROM transactions
        WHERE amount < 0
    ),
    pay_summary AS (
        SELECT m.month,
            COUNT(m.month) AS n_transactions,
            SUM(p.amount) AS amount
        FROM months m
            LEFT JOIN payments p ON m.month = p.month
        GROUP BY m.month
    ),
    fees AS (
        SELECT month,
            CASE
                WHEN amount <= -100
                AND n_transactions >= 3 THEN 0
                ELSE 5
            END AS fee
        FROM pay_summary
    ),
    t_with_fees AS (
        SELECT f.month,
            MIN(f.fee) AS fee,
            SUM(t.amount) amount
        FROM fees f
            LEFT JOIN transactions t ON f.month = TO_CHAR(t.date, 'YYYY-MM')
        GROUP BY f.month
    )
SELECT SUM(amount) - SUM(fee) AS balance
FROM t_with_fees;