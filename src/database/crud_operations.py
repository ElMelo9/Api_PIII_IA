from database.supabase_connection import supabase_client



class  Crud:

    #insert
    def create_role(self,data):
        response, error = supabase_client.table('roles').upsert(data).execute()
        if error:
            return error
        return response
    
    def create_user(self,data):
        response, error = supabase_client.table('users').upsert(data).execute()
        if error:
            return error
        return response

    def create_document(self,data):
        response, error = supabase_client.table('type_doc').upsert(data).execute()
        if error:
            return error
        return response  
     
    def create_data(self,data):
        response, error = supabase_client.table('environmental_data').upsert(data).execute()
        if error:
            return error
        return response 
    
    #select
    def get_roles(self):
        response= supabase_client.table('roles').select('*').execute()
        assert len(response.data) > 0

        data = response.data

        return data

    def get_tipoDoc(self):
        response= supabase_client.table('type_doc').select('*').execute()
        assert len(response.data) > 0

        data = response.data

        return data
    
    def get_users(self):
        response= supabase_client.table('users').select('*').execute()
        assert len(response.data) > 0

        data = response.data

        return data   

    def get_data(self):
        response= supabase_client.table('environmental_data').select('*').execute()
        assert len(response.data) > 0

        data = response.data

        return data    
    


    def get_userByEmail(self,email):

        response= supabase_client.table('users').select('name_user,last_name_user,id_rol')\
        .eq('email_user', email) \
        .execute()
        
        assert len(response.data) > 0

        data = response.data

        return data
    

