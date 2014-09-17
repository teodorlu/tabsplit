module PrintingBasics
( prettyPrintColumns
, autoAlignLines
, Alignment (..)
) where

import Data.List (transpose, intersperse)

data Alignment = L | R

alignText :: Int -> Alignment -> String -> String
alignText width L = take width . (++ repeat ' ')
alignText width R = reverse . alignText width L . reverse

alignLine :: [Int] -> [Alignment] -> [String] -> String
alignLine a b c = foldr1 (++) (zipWith3 alignText a b c)

alignLines :: [Int] -> [Alignment] -> [[String]] -> String
alignLines widths alignments lines = unlines $ map (alignLine widths alignments) lines

findWidths :: [[String]] -> [Int]
findWidths lines = map (maximum . map length) $ transpose lines

autoAlignLines :: [Alignment] -> [[String]] -> String
autoAlignLines alignments lines = alignLines (findWidths lines) alignments lines

prettyPrintColumns :: [[String]] -> String
prettyPrintColumns lines = autoAlignLines (repeat R) (map (intersperse " | ") lines)
