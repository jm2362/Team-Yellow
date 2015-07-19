
angular.module('app')
    .controller('MainController', function($scope, $location, TemplateService, BusinessService, DomainService, $resource, $http) {

		
	$scope.domainExist = false;
        $scope.businessInfo = TemplateService.getBusinessInfo();
	$scope.hostname = $scope.businessInfo.hostname;
        $scope.changeBussinessInfo = function(type, info) {
            if (type == 'businessName')       TemplateService.setBusinessName(info);
            else if (type == 'businessEmail') TemplateService.setBusinessEmail(info);
            else if (type == 'phoneNumber')   TemplateService.setPhoneNumber(info);
            else if (type == 'domainName')    TemplateService.setDomainName(info);
            $scope.businessInfo = TemplateService.getBusinessInfo();
        };
	$scope.registerDomain = function(info, form_valid) {
	    if (form_valid) {
		var path = $location.path();
		info.template = path.substring(1, path.length);
		BusinessService.register({domain: info.domainName}, {
		    businessName: info.businessName,
		    businessEmail: info.businessEmail,
		    phoneNumber: info.phoneNumber,
		    template: info.template,
		    
		}).$promise.then(function(result) {
		    console.log(info.template);
		    console.log(result);
		});
	
	    }
	}
	$scope.$watch('businessInfo.domainName', function(domain) {
	    if (domain !== undefined || domain !== "") {
		DomainService.get({domain:domain}).$promise.then(function(result) {
		    console.log("domain: " + domain + " result: ");
		    console.log(result);
		    $scope.domainExist = result.result;
		});
		
	    }
	    else
		$scope.domainExist = false;
	})
    })
