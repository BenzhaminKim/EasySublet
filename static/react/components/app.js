import React, { Component } from 'react';
import GoogleMap from './google_map';
import GoogleMapHook from './googleMapHook.js'
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
            <div style={{ width: '100%' }}>
                <h1>sadsada</h1>
                <h2>asdsadd</h2>
                <GoogleMapHook/>
            </div>
            );
    }
}