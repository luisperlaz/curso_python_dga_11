import gdata.youtube
import gdata.youtube.service

def informacionDeVideo(video): # Si se le suministra un objeto video mostrara por pantalla cierta informacion de este
 print "El nombre del video es: "+video.media.title.text
 print "Numero de reproducciones: ",video.statistics.view_count
 print "Etiquetas del video: "+video.media.keywords.text
 print

youtubeService = gdata.youtube.service.YouTubeService() # Se inicializa el objeto YouTubeService
feedDeVideos = youtubeService.GetMostViewedVideoFeed() # Se obtiene el feed de los videos mas vistos
for video in  feedDeVideos.entry: # Para cada video dentro del feed ...
  informacionDeVideo(video)
