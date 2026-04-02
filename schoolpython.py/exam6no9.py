prefix='INV'
item_id=45
checksum=239
item_id=f'{item_id:04d}'
checksum_hex=format(checksum,'x')
print(f'{prefix}-{item_id}-{checksum_hex}')