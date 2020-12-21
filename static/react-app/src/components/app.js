import React, { Component } from 'react';
import GoogleMap from './googleMap.js';
import RoomList from './RoomList.js';

export default class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            lat: 43.5487,
            lng: -79.6629
        };

        
    }    

    componentDidMount() { 
        
    }


    render() {
        return (
            <div className="row" style={{ width: '100%' }}>
                <div className="col-3">
                    <RoomList/>
                </div>
                <div className="col-9">
                    <GoogleMap/>
                </div>
            </div>
            );
    }
}