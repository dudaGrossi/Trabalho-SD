from googleapiclient.discovery import build

# Substitua 'YOUR_API_KEY' com a sua chave de API
api_key = "XXXXXXXXXXXXXX"
youtube = build('youtube', 'v3', developerKey=api_key)


def getComments(video_id):
    # Exemplo para listar os comentários de um vídeo
    response = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=6
    ).execute()

    #Cria uma lista de comentários
    comments = []

    #Preenche a lista de comentários com os atributos 'Autor' e 'Comentário'
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textOriginal']
        author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
        comments.append({'author': author, 'comment': comment})

    
    for comment in comments:
        print('-'*110)
        print(f'Autor: {comment["author"]}')
        print(f'Comentário: {comment["comment"]}')
        
    print('-'*110)

    return comments

def search_videos(assunto, max_results=5):
    response = youtube.search().list(
        q=assunto,
        type='video',
        part='snippet',
        maxResults=max_results
    ).execute()

    videos = []

    for item in response['items']:
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        videos.append({'title': title, 'video_id': video_id})

    return videos

# Exemplo de uso
'''resultados = search_videos('musica triste', max_results=5)
for video in resultados:
    print(f'Título: {video["title"]}')
    print(f'ID do Vídeo: {video["video_id"]}')
    videoid = video["video_id"]
    getComments(videoid)
    print('*' * 80)
    print("\n\n")
'''
