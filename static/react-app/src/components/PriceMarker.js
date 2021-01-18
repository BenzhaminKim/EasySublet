import React, { useState } from 'react';
import {Link} from 'react-router-dom';

function PriceMarker({roomId,price}) {

  return (
    <a  className="btn btn-success" href={'http://ec2-15-164-226-5.ap-northeast-2.compute.amazonaws.com/room/detail/'+roomId } >
      <b>$ {price}</b>
    </a>
  );
}

export default PriceMarker