-- 코드를 입력하세요
SELECT CONCAT('/home/grep/src/',UGF.BOARD_ID, '/', UGF.FILE_ID,UGF.FILE_NAME, UGF.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_BOARD AS UGB, USED_GOODS_FILE AS UGF
WHERE UGB.BOARD_ID = UGF.BOARD_ID 
AND UGB.VIEWS = (SELECT MAX(USED_GOODS_BOARD.VIEWS) FROM USED_GOODS_BOARD)
ORDER BY UGF.FILE_ID DESC


# SELECT concat('/home/grep/src/',f.board_id,'/',f.file_id, f.file_name, f.file_ext) as file_path
# from used_goods_file f 
# join used_goods_board b
# on f.board_id = b.board_id
# where b.views = (select max(b1.views) from used_goods_board b1 )
# order by f.file_id desc