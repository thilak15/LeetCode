select w1.id from Weather w1 join weather w2 on  Datediff(w1.recordDate,w2.recordDate)=1 where w1.temperature>w2.temperature