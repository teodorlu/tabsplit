import Data.List
import Data.List.Split

maketwolists :: (Num a, Ord a) => [(String, a)] -> ([(String, a)], [(String, a)])
maketwolists = partition (\x -> balance x <= 0)

balance = snd
person = fst

findpayments :: (Num a, Ord a) => [(String, a)] -> [(String, a)] -> [(String, String, a)]
findpayments (payer:xs) (payee:ys)
    | - balance payer > balance payee = first:findpayments ((person payer, balance payer + amount):xs) ys
    | - balance payer < balance payee = first:findpayments xs ((person payee, balance payee - amount):ys)
    | otherwise                                     = first:findpayments xs ys
    where
       first = (person payer, person payee, amount)
       amount = min (- balance payer) (balance payee)
findpayments [] _ = []
findpayments _ [] = []

main = do
    a <- getContents
    putStrLn $ unlines $ map (\(x,y,z) -> x ++ " -> " ++ y ++ ": " ++  show z) $ uncurry findpayments $ maketwolists $ map ((\(x:y:ys) -> (x, read y :: Float)) . splitOn ":") (lines a)
