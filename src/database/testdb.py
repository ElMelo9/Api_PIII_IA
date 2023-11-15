from supabase_connection import supabase_client


data = supabase_client.table("type_doc").select('id_typedoc','name_typedoc').execute()
# Assert we pulled real data.
assert len(data.data) > 0
print(data)
