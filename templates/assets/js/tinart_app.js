var selectedPlayer;

function initApp() {
    welcomeScreen = new welcomeScreenModal;
    welcomeScreen.init();
}

function newSimulation() {
    welcomeScreen.dismiss();
    playerSelectionScreen = new playerSelectionView;
    playerSelectionScreen.init();
}

function openSettings() {
    console.log("Open settings");
}

function selectPlayer(player) {
    selectedPlayer = player;
    // topic selection disabled for MVP
    // openTopicSelection();
    playerSelectionScreen.dismiss();
    discussionScreen = new discussionView;
    discussionScreen.init();
}

function openTopicSelection() {
    playerSelectionScreen.dismiss();
    topicSelectionScreen = new topicSelectionView;
    topicSelectionScreen.init();
} 

function startDiscussionMode() {
    topicSelectionScreen.dismiss();
    discussionScreen = new discussionView;
    discussionScreen.init();
}



class welcomeScreenModal {
    constructor() {

    }

    template = `<div class="welcome-box">
                    <div class="logo-big"></div>
                    <button color="red" size="big" onclick="newSimulation()">
                        New simulation
                    </button>
                    <button color="red" size="big" onclick="openSettings()">
                        Settings
                    </button>
                </div>`;

    init() {
        var bodyElement = document.getElementsByTagName('body')[0];
        var modalElement = document.createElement('div');
        modalElement.innerHTML = this.template;
        bodyElement.appendChild(modalElement);
    }

    dismiss() {
        var modalElement = document.getElementsByClassName('welcome-box')[0];
        modalElement.parentElement.removeChild(modalElement);
    }
}

class playerSelectionView {
    constructor() {
    }

    playerTemplate;
    playerTemplate = this.getPlayersTemplate();
    
    getPlayersTemplate() {
        var players = [
            {
                firstName: 'Christian',
                secondName: 'Lindner',
                pictureUrl: './assets/img/politicians/001.jpg',
                politicalParty: 'FDP'
            },
            {
                firstName: 'Sahra',
                secondName: 'Wagenknect',
                pictureUrl: './assets/img/politicians/002.png',
                politicalParty: 'LINKE'
            }
        ];

        var value = '';
        players.forEach((player) => {
            value += `<div class="player" (click)="selectPlayer('${player}');">
                        <div class="picture" style="background-image: url(${player.pictureUrl});"></div>
                        <p type="lead">
                            <b>${player.firstName} ${player.secondName}</b>
                        </p>
                        <p>
                            ${player.politicalParty}
                        </p>
                    </div>`;
        });

        return value;
    };

    selectPlayer(player) {
        console.log(player);
    }


    template = `<div class="select-player">
                    <h3>Select player</h3>
                    <div class="players-box">
                        ${this.playerTemplate}
                    </div>
                    <button color="red" size="big" onclick="selectPlayer('PLAYER')">
                        Next
                    </button>
                </div>`;

    init() {
        var bodyElement = document.getElementsByTagName('body')[0];
        var modalElement = document.createElement('div');
        modalElement.innerHTML = this.template;
        bodyElement.appendChild(modalElement);
    }

    dismiss() {
        var modalElement = document.getElementsByClassName('select-player')[0];
        modalElement.parentElement.removeChild(modalElement);
    }

    se
}

class topicSelectionView {
    constructor() {

    }

    topicsTemplate = [];
    topicsTemplate = this.getTopicsTemplate();

    getTopicsTemplate() {
        var topics = [
            {
                title: 'Climate change'
            },
            {
                title: 'Equal rights'
            },
            {
                title: 'Migration policy'
            },
            {
                title: 'Digitalisation'
            },
            {   
                title: 'Weapons Laws'
            }

        ];

        var value = '';
        topics.forEach((topic) => { 
            value += ` <button color="red" size="big" onclick="startDiscussionMode()">
                            ${topic.title}
                        </button>`;
        });

        return value;
    }

    template = `<div class="select-player">
                    <h3>Select topic</h3>
                    ${this.topicsTemplate}
                </div>`;

    init() {
        var bodyElement = document.getElementsByTagName('body')[0];
        var modalElement = document.createElement('div');
        modalElement.innerHTML = this.template;
        bodyElement.appendChild(modalElement);
    }

    dismiss() {
        var modalElement = document.getElementsByClassName('select-player')[0];
        modalElement.parentElement.removeChild(modalElement);
    }
}

class discussionView {
    constructor() {

    }

    template = `<div class="discussion-view">
                    <div class="speaker"></div>
                    <div class="subtitles">
                        <mark>
                            <b>[Moderator] </b>
                            Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.
                        </mark>
                    </div>
                    <div class="chatbox">
                        <button class="settings" color="red">
                            <img src="../assets/img/icons/settings.svg">
                        </button>
                        <input placeholder="Type your message...">
                        </input>
                        <button class="send" color="red">
                            <img src="../assets/img/icons/send.svg">
                        </button>
                    </div>
                </div>`;

    init() {
        var bodyElement = document.getElementsByTagName('body')[0];
        var modalElement = document.createElement('div');
        modalElement.innerHTML = this.template;
        bodyElement.appendChild(modalElement);
    }

    dismiss() {
        var modalElement = document.getElementsByClassName('discussion-view')[0];
        modalElement.parentElement.removeChild(modalElement);
    }
}

initApp();
//startDiscussionMode();