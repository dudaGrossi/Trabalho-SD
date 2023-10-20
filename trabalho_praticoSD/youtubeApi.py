from googleapiclient.discovery import build

# Substitua 'YOUR_API_KEY' com a sua chave de API
api_key = "XXXXXXXXXXXXXXXXXXXXXXX"
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