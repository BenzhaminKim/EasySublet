import React, { useState, useRef } from 'react';
import GoogleMapReact from 'google-map-react';
import useSwr from "swr";
import useSupercluster from 'use-supercluster';

const fetcher = (...args) => fetch(...args).then(response => response.json());

const Marker = ({children}) => children;

export default function GoogleMap(props) {
  // setup map
  const mapRef = useRef();
  const [zoom,setZoom] = useState(10);
  const [bounds,setBounds] = useState(null);

  // load and prepare data
  const url =
  "http://localhost:8000/api/room/all";
  const {data, error} = useSwr(url, fetcher);
  const rooms = data && !error ? data : [];
  const points = rooms.map(room =>({
      type: "Feature",
      properties:{
          cluster: false,
          roomId: room.id,
          roomPrice: room.price,
          
      },
      geometry:{ 
          type: "Point", 
          coordinates:[
          parseFloat(room.longitude),
          parseFloat(room.latitude)
      ]
    }
  }));
  // get map bounds

  // get clusters
  const { clusters,supercluster  } = useSupercluster({
      points,
      bounds,
      zoom,
      options: { radius: 75, maxZoom: 20}
  })
  // return map
  return (
    <div style={{ height: "94vh", width: "100%" }}>
      <GoogleMapReact
        bootstrapURLKeys={{ key: 'AIzaSyDrXGchsr2Z6YkgR5WLTvDhBAfU00aMYf8' }}
        defaultCenter={{ lat: 43.6532, lng: -79.335171 }}
        defaultZoom={10}
        yesIWantToUseGoogleMapApiInternals
        onGoogleApiLoaded={({map})=>{
            mapRef.current = map;
        }}
        onChange={({zoom, bounds})=>{
            setZoom(zoom);
            setBounds([
                bounds.nw.lng,
                bounds.se.lat,
                bounds.se.lng,
                bounds.nw.lat
            ]);
            props.onChange(bounds)
        }}
      >
          {clusters.map(cluster => {
              const [longitude,latitude] = cluster.geometry.coordinates;
              const {cluster: isCluster, point_count: pointCount} = cluster.properties;
              if(isCluster){
                return(
                <Marker key={cluster.id} lat={latitude} lng={longitude}>
                    <div className="cluster-marker" 
                    onClick={()=>{
                        const expansionZoom = Math.min(
                            supercluster.getClusterExpansionZoom(cluster.id),
                            20
                        );
                        mapRef.current.setZoom(expansionZoom);
                        mapRef.current.panTo({lat:latitude, lng:longitude})
                    }}
                    >
                        {pointCount}
                    </div>
                </Marker>
                );
              }
              return(
                <Marker key={cluster.properties.roomId} lat={latitude} lng={longitude}>
                    <button className="btn btn-success">
                        <b>$ {cluster.properties.roomPrice}</b>
                    </button>
                </Marker>
              );
          })}

      </GoogleMapReact>
    </div>
  );
}
