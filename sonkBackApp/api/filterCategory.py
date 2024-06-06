class filterCategory: 
    
        
    def verfiyFilters( filter: str): 
        filters = ["songs", "videos", "albums", "artists", "playlists", "community_playlists", "featured_playlists", "uploads", "profiles", "podcasts", "episodes"]
        try:
            if filter in  filters:
                return True
            else: 
                return False
        except Exception as e:  
            return False
    