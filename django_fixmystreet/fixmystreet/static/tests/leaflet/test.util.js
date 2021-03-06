/* jshint expr: true */

var expect = chai.expect;


describe('L.FixMyStreet.Util', function () {
  var LATLNG = new L.LatLng(50.8460974, 4.3694384000000355);
  var POINT = new L.Point(LATLNG.lng, LATLNG.lat);
  var POINT_31370 = {x: 150048.32, y: 170632.53};  // Computed from LATLNG on http://epsg.io/31370/map
  var ADDRESS = {
    street: 'Avenue des Arts',
    number: '21',
    postalCode: '1000',
    city: 'Brussels',
    latlng: LATLNG,
  };
  var URBIS_ADDRESS_FROM_LATLNG_RESULT = {
    adNc: '10005006  21',
    address: {
      number: '21',
      street: {
        id: '5583',
        name: 'Avenue des Arts',
        postCode: '1000',
      },
    },
    addresspointid: '2108357',
    geocodematchcode: 1,
    point: {
      x: 4.369348321556435,
      y: 50.84611094405465,
    },
    streetaxisid: '11026560',
    streetsectionid: '11026504',
  };


  var _expectOriginalAddress = function (result) {
    expect(result.street.toLowerCase()).to.be.equal(ADDRESS.street.toLowerCase());
    expect(result.number.toLowerCase()).to.be.equal(ADDRESS.number.toLowerCase());
    expect(result.postalCode.toLowerCase()).to.be.equal(ADDRESS.postalCode.toLowerCase());
    expect(result.city.toLowerCase()).to.be.equal(ADDRESS.city.toLowerCase());
    expect(result.latlng.lat).to.be.closeTo(ADDRESS.latlng.lat, 0.0001);
    expect(result.latlng.lng).to.be.closeTo(ADDRESS.latlng.lng, 0.0001);
  };


  it('should initialize correclty', function () {
    expect(LATLNG).to.be.instanceOf(L.LatLng);
    expect(POINT).to.be.instanceOf(L.Point);
  });


  describe('_initProj4js', function () {
    it('should convert correctly', function () {
      expect(L.FixMyStreet.Util.PROJ4JS_4326).to.be.undefined;
      expect(L.FixMyStreet.Util.PROJ4JS_31370).to.be.undefined;

      L.FixMyStreet.Util._initProj4js();
      expect(L.FixMyStreet.Util.PROJ4JS_4326).to.be.instanceOf(Proj4js.Proj);
      expect(L.FixMyStreet.Util.PROJ4JS_31370).to.be.instanceOf(Proj4js.Proj);
    });
  });


  describe('toLatLng', function () {
    var _checkToLatLng = function (value) {
      var result = L.FixMyStreet.Util.toLatLng(value);
      expectLatLngEqual(result, LATLNG);
    };

    var _expectException = function (value) {
      var fn = function () {
        L.FixMyStreet.Util.toLatLng(value);
      };
      expect(fn).to.throw(TypeError);
    };

    it('should accept undefined and null', function () {
      expect(L.FixMyStreet.Util.toLatLng(undefined)).to.be.undefined;
      expect(L.FixMyStreet.Util.toLatLng(null)).to.be.null;
    });

    it('should accept a L.LatLng', function () {
      var result = L.FixMyStreet.Util.toLatLng(LATLNG);
      expect(result).to.be.instanceOf(L.LatLng);
      expect(result).to.be.equal(LATLNG);
    });

    it('should accept a L.Point', function () {
      _checkToLatLng(POINT);
    });

    it('should accept a string "Lat,Lng"', function () {
      var str = LATLNG.lat + ',' + LATLNG.lng;
      expect(str).to.be.a('string');
      _checkToLatLng(str);
    });

    it('should accept a string "Lat, Lng"', function () {
      var str = LATLNG.lat + ', ' + LATLNG.lng;
      expect(str).to.be.a('string');
      _checkToLatLng(str);
    });

    it('should accept a LatLng dictionary {lat: Lat, lng: Lng}', function () {
      var obj = {lat: LATLNG.lat, lng: LATLNG.lng};
      _checkToLatLng(obj);
    });

    it('should accept a LatLng array [Lat, Lng]', function () {
      var obj = [LATLNG.lat, LATLNG.lng];
      _checkToLatLng(obj);
    });

    it('should accept a Point dictionary {x: X, y: Y}', function () {
      var obj = {x: POINT.x, y: POINT.y};
      _checkToLatLng(obj);
    });

    it('should throw an Error otherwise', function () {
      _expectException('invalid, value');
      _expectException('invalid-value');

      _expectException({lat: 'invalid-value', lng: 123});
      _expectException({lat: 'invalid-value', key: 123});

      _expectException(['invalid-value', 123.45]);

      _expectException({x: 'invalid-value', y: 123});
      _expectException({x: 'invalid-value', key: 123});
    });
  });


  describe('toPoint', function () {
    var _checkToPoint = function (value) {
      var result = L.FixMyStreet.Util.toPoint(value);
      expectPointEqual(result, POINT);
    };

    var _expectException = function (value) {
      var fn = function () {
        L.FixMyStreet.Util.toPoint(value);
      };
      expect(fn).to.throw(TypeError);
    };

    it('should accept undefined and null', function () {
      expect(L.FixMyStreet.Util.toPoint(undefined)).to.be.undefined;
      expect(L.FixMyStreet.Util.toPoint(null)).to.be.null;
    });

    it('should accept a L.Point', function () {
      var result = L.FixMyStreet.Util.toPoint(POINT);
      expect(result).to.be.instanceOf(L.Point);
      expect(result).to.be.equal(POINT);
    });

    it('should accept a L.LatLng', function () {
      _checkToPoint(LATLNG);
    });

    it('should accept a string "X,Y"', function () {
      var str = POINT.x + ', ' + POINT.y;
      expect(str).to.be.a('string');
      _checkToPoint(str);
    });

    it('should accept a Point dictionary {x: X, y: Y}', function () {
      var obj = {x: POINT.x, y: POINT.y};
      _checkToPoint(obj);
    });

    it('should accept a Point array [X, Y]', function () {
      var obj = [POINT.x, POINT.y];
      _checkToPoint(obj);
    });

    it('should accept a LatLng dictionary {lat: Lat, lng: Lng}', function () {
      var obj = {lat: LATLNG.lat, lng: LATLNG.lng};
      _checkToPoint(obj);
    });

    it('should throw an Error otherwise', function () {
      _expectException('invalid, value');
      _expectException('invalid-value');

      _expectException({x: 'invalid-value', y: 123});
      _expectException({x: 'invalid-value', key: 123});

      _expectException(['invalid-value', 123.45]);

      _expectException({lat: 'invalid-value', lng: 123});
      _expectException({lat: 'invalid-value', key: 123});
    });
  });


  describe('fromUrbisCoords', function () {
    it('should convert correctly', function () {
      var result = L.FixMyStreet.Util.fromUrbisCoords(POINT_31370);
      expectPointEqual(result, POINT, 0.0000008);  // Min: 0.00000065
    });
  });


  describe('toUrbisCoords', function () {
    it('should convert correctly', function () {
      var result = L.FixMyStreet.Util.toUrbisCoords(POINT);
      expectPointEqual(result, POINT_31370, 0.08);  // Min: 0.065
    });
  });


  describe('urbisCoordsToLatLng', function () {
    it('should convert correctly', function () {
      var result = L.FixMyStreet.Util.urbisCoordsToLatLng(POINT_31370);
      expectLatLngEqual(result, LATLNG, 0.0000008);  // Min: 0.00000065
    });
  });


  describe('getAddressFromLatLng', function () {
    it('should convert correctly', function (done) {
      L.FixMyStreet.Util.getAddressFromLatLng(LATLNG, function (result) {
        asyncExpect(done, function () {
          _expectOriginalAddress(result);
          done();
        });
      });
    });
  });


  describe('urbisResultToAddress', function () {
    it('should convert correctly', function () {
      var result = L.FixMyStreet.Util.urbisResultToAddress(URBIS_ADDRESS_FROM_LATLNG_RESULT);
      _expectOriginalAddress(result);
    });
  });


  describe('getStreetViewUrl', function () {
    // @TODO: How to test that?
  });


  describe('_toProj4jsPoint', function () {
    it('should convert correctly', function () {
      var result = L.FixMyStreet.Util._toProj4jsPoint(POINT);
      expect(result).to.be.instanceOf(Proj4js.Point);
      expect(result.x).to.be.equal(POINT.x);
      expect(result.y).to.be.equal(POINT.y);
    });
  });
});
