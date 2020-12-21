import React, { useState } from 'react';
import GoogleMapReact from 'google-map-react';

function GoogleMap() {
  // Declare a new state variable, which we'll call "count"
  const [count, setCount] = useState(0);

  return (
    <div style={{ height: '100vh', width: '100%' }}>
    <GoogleMapReact
      bootstrapURLKeys={{ key: 'AIzaSyDrXGchsr2Z6YkgR5WLTvDhBAfU00aMYf8' }}
      defaultCenter={{lat:43.6532,lng:-79.3832}}
      defaultZoom={11}
    >
    </GoogleMapReact>
  </div>
  );
}

export default GoogleMap