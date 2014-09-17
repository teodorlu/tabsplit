import Data.List
import Data.List.Split
import Text.Printf
import PrintingBasics

balance = snd
person = fst

makeTwoLists :: [(a, Float)] -> ([(a, Float)], [(a, Float)])
makeTwoLists = partition (\x -> balance x <= 0)

findPayments :: (Ord b, Num b) => [(a, b)] -> [(a1, b)] -> [(a, a1, b)]
findPayments (payer:xs) (payee:ys)
    | - balance payer > balance payee = first:findPayments ((person payer, balance payer + amount):xs) ys
    | - balance payer < balance payee = first:findPayments xs ((person payee, balance payee - amount):ys)
    | otherwise                       = first:findPayments xs ys
    where
       first = (person payer, person payee, amount)
       amount = min (- balance payer) (balance payee)
findPayments _ _ = []

printEntry (payer, payee, amount) = [payer, " -> ", payee ++ ": ", printf "%.2f" amount, " kr"]
printEntries = unlines . sort . lines . autoAlignLines [L, L, L, R, L] . map printEntry

main = do
    a <- getContents
    putStr . printEntries . uncurry findPayments . makeTwoLists $ map ((\(x:y:ys) -> (x, read y :: Float)) . splitOn ":") (lines a)
