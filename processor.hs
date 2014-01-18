balance = snd
person = fst

findpayments :: (Num a, Ord a) => [(String, a)] -> [(String, a)] -> [(String, String, a)]
findpayments (payer:xs) (payee:ys)
    | (abs . balance) payer > (abs . balance) payee = first:(findpayments ((person payer, (balance payer) - amount):xs) ys)
    | (abs . balance) payer < (abs . balance) payee = first:(findpayments xs ((person payee, (balance payee) + amount):ys))
    | otherwise                                     = first:(findpayments xs ys)
    where
       first = (person payer, person payee, amount)
       amount = min (balance payer) ((abs . balance) payee)
findpayments [] [] = []


t1 = [("Erik", 120.5), ("Teodor", 10.5)]
t2 = [("Cecilie", -20.5), ("Kristina", -110.5)]
