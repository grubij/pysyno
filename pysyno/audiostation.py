"""
Browse.Playlist
VoiceAssistant.Browse
VoiceAssistant.Challenge
VoiceAssistant.Info
VoiceAssistant.Stream
WebPlayer
"""

from .base import BaseApi


# class Album(BaseApi):
#     def __init__(self, parent):
#         super(Album, self).__init__(apiname='SYNO.AudioStation.Album', parent=parent)
#
#
# class Artist(BaseApi):
#     def __init__(self, parent):
#         super(Artist, self).__init__(apiname='SYNO.AudioStation.Artist', parent=parent)
#
#
# class Browse(BaseApi):
#     def __init__(self, parent):
#         super(Browse, self).__init__(apiname='SYNO.AudioStation.Browse', parent=parent)
#
#
# class Composer(BaseApi):
#     def __init__(self, parent):
#         super(Composer, self).__init__(apiname='SYNO.AudioStation.Composer', parent=parent)
#
#
# class Cover(BaseApi):
#     def __init__(self, parent):
#         super(Cover, self).__init__(apiname='SYNO.AudioStation.Cover', parent=parent)
#
#
# class Download(BaseApi):
#     def __init__(self, parent):
#         super(Download, self).__init__(apiname='SYNO.AudioStation.Download', parent=parent)
#
#
# class Folder(BaseApi):
#     def __init__(self, parent):
#         super(Folder, self).__init__(apiname='SYNO.AudioStation.Folder', parent=parent)
#
#
# class Genre(BaseApi):
#     def __init__(self, parent):
#         super(Genre, self).__init__(apiname='SYNO.AudioStation.Genre', parent=parent)
#
#
# class Info(BaseApi):
#     def __init__(self, parent):
#         super(Info, self).__init__(apiname='SYNO.AudioStation.Info', parent=parent)
#
#
# class Lyrics(BaseApi):
#     def __init__(self, parent):
#         super(Lyrics, self).__init__(apiname='SYNO.AudioStation.Lyrics', parent=parent)
#
#
# class LyricsSearch(BaseApi):
#     def __init__(self, parent):
#         super(LyricsSearch, self).__init__(apiname='SYNO.AudioStation.LyricsSearch', parent=parent)
#
#
# class MediaServer(BaseApi):
#     def __init__(self, parent):
#         super(MediaServer, self).__init__(apiname='SYNO.AudioStation.MediaServer', parent=parent)
#
#
# class Pin(BaseApi):
#     def __init__(self, parent):
#         super(Pin, self).__init__(apiname='SYNO.AudioStation.Pin', parent=parent)


class Playlist(BaseApi):
    def __init__(self, parent):
        super(Playlist, self).__init__(apiname='SYNO.AudioStation.Playlist', parent=parent)

    def list(self, library: str = 'all', sort_by: str = 'title', sort_direction: str = 'ASC'):
        """List available playlists.

        :param library: Library to parse (personal or all)
        :type library: str
        :param sort_by: What attribute to sort by
        :type sort_by: str
        :param sort_direction: Direction to sort by (ASC or DESC)#
        :type sort_direction: str
        :return: Request result
        :rtype: dict
        """
        params = {
            'library': library,
            'sort_by': sort_by,
            'sort_direction': sort_direction
        }
        return self.request('list', **params)


# class Proxy(BaseApi):
#     def __init__(self, parent):
#         super(Proxy, self).__init__(apiname='SYNO.AudioStation.Proxy', parent=parent)


class Radio(BaseApi):
    def __init__(self, parent):
        super(Radio, self).__init__(apiname='SYNO.AudioStation.Radio', parent=parent)

    def list(self, library: str = 'all', container: str = 'Favorite', sort_by: str = 'title', sort_direction: str = 'ASC'):
        """List available radio stations.

        :param library: The library to search (personal or all)
        :type library: str
        :param container: The container to search (e.g. Favorites)
        :type container: str
        :param sort_by: What attribute to sort by
        :type sort_by: str
        :param sort_direction: Direction to sort by (ASC or DESC)#
        :type sort_direction: str
        :return: Request result
        :rtype: dict
        """
        params = {
            'library': library,
            'container': container,
            'sort_by': sort_by,
            'sort_direction': sort_direction
        }
        return self.request('list', **params)


class RemotePlayer(BaseApi):
    def __init__(self, parent):
        super(RemotePlayer, self).__init__(apiname='SYNO.AudioStation.RemotePlayer', parent=parent)

    def list(self, type: str = 'all', additional: str = 'subplayer_list'):
        """Lists the available remote players.

        :param type: Type of remote players to list
        :type type: str
        :param additional: TODO: Add parameter documentation
        :type additional: str
        :return: Request result
        :rtype: dict
        """
        params = {
            'type': type,
            'additional': additional
        }
        return self.request('list', **params)

    def control(self, id: str, action: str, value: str):
        """Controls a remote players by its id and executing a specific actions with a given value.

        Available control actions and possible values:
        - play (101)
        - set_shuffle (true/false)

        :param id: Remote player id
        :type id: str
        :param action: The action to perform on the remote player
        :type action: str
        :param value: The value for the action
        :type value: str
        :return: Request result
        :rtype: dict
        """
        params = {
            'id': id,
            'action': action,
            'value': value
        }
        return self.request('control', **params)


class RemotePlayerStatus(BaseApi):
    def __init__(self, parent):
        super(RemotePlayerStatus, self).__init__(apiname='SYNO.AudioStation.RemotePlayerStatus', parent=parent)

    def list(self, type: str = 'all', additional: str = 'subplayer_list'):
        """Lists the available remote players.

        :param type: Type of remote players to list
        :type type: str
        :param additional: TODO: Add parameter documentation
        :type additional: str
        :return: Request result
        :rtype: dict
        """
        params = {
            'type': type,
            'additional': additional
        }
        return self.request('list', **params)


# class Search(BaseApi):
#     def __init__(self, parent):
#         super(Search, self).__init__(apiname='SYNO.AudioStation.Search', parent=parent)
#
#
# class Song(BaseApi):
#     def __init__(self, parent):
#         super(Song, self).__init__(apiname='SYNO.AudioStation.Song', parent=parent)
#
#
# class Stream(BaseApi):
#     def __init__(self, parent):
#         super(Stream, self).__init__(apiname='SYNO.AudioStation.Stream', parent=parent)
#
#
# class Tag(BaseApi):
#     def __init__(self, parent):
#         super(Tag, self).__init__(apiname='SYNO.AudioStation.Tag', parent=parent)


class AudioStation:
    def __init__(self, parent):
        self.parent = parent
        self.host = self.parent.host
        self.verify_ssl = self.parent.verify_ssl
        self.Playlist = Playlist(self)
        self.Radio = Radio(self)
        self.RemotePlayer = RemotePlayer(self)
        self.RemotePlayerStatus = RemotePlayerStatus(self)
